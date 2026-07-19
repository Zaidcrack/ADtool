from core.logger import info, success
from core.report import show_report

from AD.plugins import smb
from AD.plugins import ldap
from AD.plugins import kerberos
from AD.plugins import dns
from AD.plugins import rpc
from AD.plugins import winrm
from AD.plugins import gc
from AD.plugins import adws
from AD.plugins import ldaps

def run(target):

    info(f"Iniciando escaneo AD contra {target}")

    results = {}

    results["smb"] = smb.check(
        target,
        445,
        3
    )

    results["ldap"] = ldap.enum(
        target,
        389
    )

    results["kerberos"] = kerberos.check(
        target,
        88
    )

    results["dns"] = dns.enum(
        target,
        53
    )
    
    results["rpc"] = rpc.check(
        target,
       135
    )
    results["winrm"] = winrm.check(target, 5985)

    results["ldaps"] = ldaps.check(target, 636)

    results["gc"] = gc.check(target, 3268)

    results["adws"] = adws.check(target, 9389)
    
    success("Escaneo terminado")
    show_report(results)

    return results
