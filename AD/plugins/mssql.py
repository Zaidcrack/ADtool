from core.logger import info, success, warning
from core.network import check_tcp


def check(target, port=1433):

    info(f"Objetivo MSSQL: {target}")
    info(f"Puerto: {port}")

    if check_tcp(target, port):

        success("MSSQL disponible")

        return {
            "target": target,
            "protocol": "MSSQL",
            "status": "online",
            "port": port
        }

    warning("MSSQL no disponible")

    return {
        "target": target,
        "protocol": "MSSQL",
        "status": "offline",
        "port": port
    }
