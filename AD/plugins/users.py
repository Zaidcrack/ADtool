from ldap3 import Server, Connection, ALL, NTLM

from core.logger import info, success, warning, error
from core.network import check_tcp


def enum(
    target,
    port=389,
    username="",
    password="",
    domain=""
):
    info(f"Objetivo LDAP: {target}")
    info(f"Enumerando usuarios en {target}")

    if not check_tcp(target, port):
        warning(f"LDAP no disponible en puerto {port}")
        return {
            "target": target,
            "port": port,
            "protocol": "LDAP Users",
            "status": "offline",
            "users": []
        }

    try:
        server = Server(
            target,
            port=port,
            get_info=ALL
        )

        if username:
            user = f"{domain}\\{username}" if domain else username

            conn = Connection(
                server,
                user=user,
                password=password,
                authentication=NTLM,
                auto_bind=True
            )
        else:
            conn = Connection(
                server,
                auto_bind=True
            )

        base_dn = server.info.other.get(
            "defaultNamingContext",
            [None]
        )[0]

        if not base_dn:
            raise RuntimeError("No se pudo obtener el Base DN")

        info(f"Base DN: {base_dn}")

        conn.search(
            search_base=base_dn,
            search_filter="(&(objectCategory=person)(objectClass=user))",
            attributes=[
                "sAMAccountName",
                "displayName",
                "distinguishedName",
                "userAccountControl"
            ]
        )

        users = []

        for entry in conn.entries:
            data = entry.entry_attributes_as_dict

            users.append({
                "username": data.get("sAMAccountName", [""])[0],
                "display_name": data.get("displayName", [""])[0],
                "dn": data.get("distinguishedName", [""])[0],
                "user_account_control": data.get(
                    "userAccountControl",
                    [None]
                )[0]
            })

        success(f"Usuarios encontrados: {len(users)}")

        conn.unbind()

        return {
            "target": target,
            "port": port,
            "protocol": "LDAP Users",
            "status": "online",
            "base_dn": base_dn,
            "count": len(users),
            "users": users
        }

    except Exception as e:
        error(f"Users error: {e}")

        return {
            "target": target,
            "port": port,
            "protocol": "LDAP Users",
            "status": "error",
            "users": [],
            "error": str(e)
        }
