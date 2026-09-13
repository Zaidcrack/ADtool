from core.logger import info, success, warning, error
from core.network import check_tcp
from impacket.smbconnection import SMBConnection


def check(target, port, timeout):

    info(f"Objetivo: {target}")
    info(f"Puerto: {port}")
    info(f"Timeout: {timeout}")

    try:

        if not check_tcp(target, port, timeout):
            warning(f"SMB no disponible en puerto {port}")

            return {
                "target": target,
                "port": port,
                "protocol": "SMB",
                "status": "offline"
            }

        success(f"SMB disponible en puerto {port}")

        conn = SMBConnection(target, target)
        conn.login("", "")

        server = conn.getServerName()
        domain = conn.getServerDomain()
        os = conn.getServerOS()

        shares = []

        try:
            for share in conn.listShares():
                shares.append(share["shi1_netname"][:-1])
        except Exception:
            pass

        conn.close()

        return {
            "target": target,
            "port": port,
            "protocol": "SMB",
            "status": "online",
            "hostname": server,
            "domain": domain,
            "os": os,
            "shares": shares
        }

    except Exception as e:
        error(f"SMB error: {e}")

        return {
            "target": target,
            "port": port,
            "protocol": "SMB",
            "status": "online"
        }
