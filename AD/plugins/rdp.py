from core.logger import info, success, warning
from core.network import check_tcp


def check(target, port=3389):

    info(f"Objetivo RDP: {target}")
    info(f"Puerto: {port}")

    if check_tcp(target, port):

        success("RDP disponible")

        return {
            "target": target,
            "protocol": "RDP",
            "status": "online",
            "port": port
        }

    warning("RDP no disponible")

    return {
        "target": target,
        "protocol": "RDP",
        "status": "offline",
        "port": port
    }
