import socket


def check_tcp(host: str, port: int, timeout: int = 3) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        sock.connect((host, port))
        return True
    except socket.error:
        return False
    finally:
        sock.close()


def check_udp(host: str, port: int, timeout: int = 3) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)

    try:
        sock.sendto(b"ADtool", (host, port))
        sock.recvfrom(1024)
        return True
    except socket.error:
        return False
    finally:
        sock.close()
