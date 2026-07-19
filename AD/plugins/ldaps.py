from core.logger import info, success, warning, error
from core.network import check_tcp


def check(target, port):
    info(f"Objetivo LDAPS: {target}")
    info(f"Puerto: {port}")

    try:
        ldaps = check_tcp(target, port)

        if ldaps:
            success(f"LDAPS disponible en puerto {port}")
        else:
            warning(f"LDAPS no disponible en puerto {port}")

        return {
            "target": target,
            "port": port,
            "protocol": "LDAPS",
            "status": "online" if ldaps else "offline"
        }

    except Exception as e:
        error(f"LDAPS error: {e}")
        return None
