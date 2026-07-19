from core.logger import info, success, warning, error
from core.network import check_tcp


def check(target, port, timeout):
    info(f"Objetivo: {target}")
    info(f"Puerto: {port}")
    info(f"Timeout: {timeout}")

    try:
        smb = check_tcp(target, port, timeout)

        if smb:
            success(f"SMB disponible en puerto {port}")
        else:
            warning(f"SMB no disponible en puerto {port}")

        return {
            "target": target,
            "port": port,
            "protocol": "SMB",
            "status": "online" if smb else "offline"
        }

    except Exception as e:
        error(f"SMB error: {e}")
        return None
