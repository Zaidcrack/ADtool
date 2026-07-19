from core.logger import info, success, warning, error
from core.network import check_tcp, check_udp


def check(target, port):
    info(f"Comprobando Kerberos en {target}")

    try:
        info(f"Puerto: {port}")

        tcp = check_tcp(target, port)
        udp = check_udp(target, port)

        if tcp:
            success(f"TCP {port} abierto")
        else:
            warning(f"TCP {port} cerrado")

        if udp:
            success(f"UDP {port} respondió")
        else:
            warning(f"UDP {port} sin respuesta")

        success("Comprobación Kerberos terminada")

        return {
            "target": target,
            "port": port,
            "protocol": "Kerberos",
            "status": "online" if tcp or udp else "offline",
            "tcp": tcp,
            "udp": udp
        }

    except Exception as e:
        error(f"Kerberos error: {e}")
        return None
