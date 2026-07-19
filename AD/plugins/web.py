import requests

from core.logger import info, success, warning
from core.network import check_tcp


def check(target):
    info(f"Objetivo Web: {target}")

    result = {
        "target": target,
        "protocol": "WEB",
        "status": "offline"
    }

    for scheme, port in [("http", 80), ("https", 443)]:

        if not check_tcp(target, port):
            continue

        try:
            url = f"{scheme}://{target}"

            r = requests.get(url, timeout=3, verify=False)

            server = r.headers.get("Server", "Desconocido")

            success(f"{scheme.upper()} disponible")
            info(f"Servidor: {server}")

            result.update({
                "status": "online",
                "port": port,
                "server": server
            })

            return result

        except Exception:
            pass

    warning("Servicio Web no disponible")

    return result
