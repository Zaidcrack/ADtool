from core.logger import info, success, warning, error
from core.network import check_tcp


def check(target, port):
    info(f"Objetivo AD Web Services: {target}")
    info(f"Puerto: {port}")

    try:
        adws = check_tcp(target, port)

        if adws:
            success(f"ADWS disponible en puerto {port}")
        else:
            warning(f"ADWS no disponible")

        return {
            "target": target,
            "port": port,
            "protocol": "ADWS",
            "status": "online" if adws else "offline"
        }

    except Exception as e:
        error(f"ADWS error: {e}")
        return None
