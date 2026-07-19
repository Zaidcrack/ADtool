from core.logger import info, success, warning, error
from core.network import check_tcp


def check(target, port):
    info(f"Objetivo WinRM: {target}")
    info(f"Puerto: {port}")

    try:
        winrm = check_tcp(target, port)

        if winrm:
            success(f"WinRM disponible en puerto {port}")
        else:
            warning(f"WinRM no disponible en puerto {port}")

        return {
            "target": target,
            "port": port,
            "protocol": "WinRM",
            "status": "online" if winrm else "offline"
        }

    except Exception as e:
        error(f"WinRM error: {e}")
        return None
