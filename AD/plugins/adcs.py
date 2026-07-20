import requests

from core.logger import info, success, warning


def check(target):

    info(f"Buscando AD CS en {target}")

    result = {
        "target": target,
        "protocol": "ADCS",
        "status": "offline",
        "port": "80/443"
    }

    paths = [
        "http://{}/certsrv/",
        "https://{}/certsrv/"
    ]

    for url in paths:

        try:

            full = url.format(target)

            r = requests.get(
                full,
                timeout=3,
                verify=False
            )

            if r.status_code in [200, 401]:

                success("AD CS encontrado")
                info(full)

                result.update({
                    "status": "online",
                    "url": full
                })

                return result

        except Exception:
            pass

    warning("AD CS no encontrado")

    return result
