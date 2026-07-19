from ldap3 import Server, Connection, ALL

from core.logger import info, success, warning, error
from core.network import check_tcp


def enum(target, port=389):
    info(f"Objetivo: {target}")
    info(f"Puerto: {port}")

    if not check_tcp(target, port):
        warning("LDAP no disponible")
        return None

    try:
        server = Server(target, port=port, get_info=ALL)
        conn = Connection(server)

        if not conn.bind():
            warning("No fue posible realizar el bind LDAP")
            return None

        success("LDAP disponible")

        base_dn = server.info.other.get(
            "defaultNamingContext",
            ["N/A"]
        )[0]

        forest = server.info.other.get(
            "rootDomainNamingContext",
            ["N/A"]
        )[0]

        configuration = server.info.other.get(
            "configurationNamingContext",
            ["N/A"]
        )[0]

        schema = server.info.other.get(
            "schemaNamingContext",
            ["N/A"]
        )[0]

        info(f"Base DN: {base_dn}")
        info(f"Forest: {forest}")
        info(f"Configuration: {configuration}")
        info(f"Schema: {schema}")

        conn.search(
            search_base=base_dn,
            search_filter="(objectClass=domain)",
            attributes=[
                "objectSid",
                "ms-DS-MachineAccountQuota",
                "minPwdLength",
                "lockoutThreshold",
                "maxPwdAge"
            ]
        )

        if conn.entries:
            entry = conn.entries[0]

            if "objectSid" in entry:
                info(f"Domain SID: {entry.objectSid}")

            if "ms-DS-MachineAccountQuota" in entry:
                info(f"MachineAccountQuota: {entry['ms-DS-MachineAccountQuota']}")

            if "minPwdLength" in entry:
                info(f"Min Password Length: {entry.minPwdLength}")

            if "lockoutThreshold" in entry:
                info(f"Lockout Threshold: {entry.lockoutThreshold}")

            if "maxPwdAge" in entry:
                info(f"Max Password Age: {entry.maxPwdAge}")

        conn.unbind()

        return {
            "status": "online",
            "base_dn": base_dn,
            "forest": forest
        }

    except Exception as e:
        error(str(e))
        return None
