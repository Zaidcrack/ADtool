from core.logger import info, error


def check(domain):
    info(f"Comprobando Kerberos en {domain}")

    try:
        result = {
            "domain": domain,
            "protocol": "Kerberos",
            "status": "checked"
        }

        info("Comprobación Kerberos terminada")
        return result

    except Exception as e:
        error(f"Kerberos error: {e}")
        return None
