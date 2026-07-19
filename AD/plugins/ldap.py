from ldap3 import Server, Connection, ALL

from core.logger import info, success, warning, error
from core.network import check_tcp


def enum(target, port):
    info(f"Objetivo LDAP: {target}")
    info(f"Puerto: {port}")

    # Comprobar que el puerto esté abierto
    if not check_tcp(target, port):
        warning(f"LDAP no disponible en puerto {port}")
        return {
            "target": target,
            "port": port,
            "protocol": "LDAP",
            "status": "offline"
        }

    try:
        server = Server(
            target,
            port=port,
            get_info=ALL
        )

        conn = Connection(server)

        if conn.bind():

            success("LDAP disponible")

            base_dn = server.info.other.get(
                "defaultNamingContext",
                ["N/A"]
            )[0]

            forest = server.info.other.get(
                "rootDomainNamingContext",
                ["N/A"]
            )[0]

            schema = server.info.other.get(
                "schemaNamingContext",
                ["N/A"]
            )[0]

            config = server.info.other.get(
                "configurationNamingContext",
                ["N/A"]
            )[0]

            ldap_version = server.info.other.get(
                "supportedLDAPVersion",
                ["N/A"]
            )

            info(f"Base DN: {base_dn}")
            info(f"Forest: {forest}")
            info(f"Configuration: {config}")
            info(f"Schema: {schema}")
            info(f"LDAP Version: {', '.join(map(str, ldap_version))}")

            conn.unbind()

            return {
                "target": target,
                "port": port,
                "protocol": "LDAP",
                "status": "online",
                "base_dn": base_dn,
                "forest": forest,
                "configuration": config,
                "schema": schema,
                "ldap_version": ldap_version
            }

        warning("No fue posible realizar el bind LDAP")

        return {
            "target": target,
            "port": port,
            "protocol": "LDAP",
            "status": "offline"
        }

    except Exception as e:

        error(f"LDAP error: {e}")

        return {
            "target": target,
            "port": port,
            "protocol": "LDAP",
            "status": "offline",
            "error": str(e)
        }
