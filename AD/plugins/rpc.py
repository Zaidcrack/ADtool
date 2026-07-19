from core.logger import info, success, warning, error
from core.network import check_tcp


def check(target, port):
    info(f"Objetivo RPC: {target}")
    info(f"Puerto: {port}")

    try:
        rpc = check_tcp(target, port)

        if rpc:
            success(f"RPC disponible en puerto {port}")
        else:
            warning(f"RPC no disponible en puerto {port}")

        return {
            "target": target,
            "port": port,
            "protocol": "RPC",
            "status": "online" if rpc else "offline"
        }

    except Exception as e:
        error(f"RPC error: {e}")
        return None
