from core.logger import info, success, warning, error
from core.network import check_tcp


def check(target, port):
    info(f"Objetivo Global Catalog: {target}")
    info(f"Puerto: {port}")

    try:
        gc = check_tcp(target, port)

        if gc:
            success(f"Global Catalog disponible en puerto {port}")
        else:
            warning(f"Global Catalog no disponible")

        return {
            "target": target,
            "port": port,
            "protocol": "Global Catalog",
            "status": "online" if gc else "offline"
        }

    except Exception as e:
        error(f"GC error: {e}")
        return None
