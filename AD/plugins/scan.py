from concurrent.futures import ThreadPoolExecutor, as_completed

from core.logger import info, success
from core.report import show_report
from core.export import export_json, export_csv

from AD.plugins import smb
from AD.plugins import ldap
from AD.plugins import kerberos
from AD.plugins import dns
from AD.plugins import rpc
from AD.plugins import winrm
from AD.plugins import gc
from AD.plugins import adws
from AD.plugins import ldaps
from AD.plugins import web
from AD.plugins import rdp
from AD.plugins import mssql
from AD.plugins import adcs


def run(target, json_output=False, csv_output=False):

    info(f"Iniciando escaneo AD contra {target}")

    results = {}

    tasks = {
        "smb": lambda: smb.check(target, 445, 3),
        "ldap": lambda: ldap.enum(target, 389),
        "kerberos": lambda: kerberos.check(target, 88),
        "dns": lambda: dns.enum(target, 53),
        "rpc": lambda: rpc.check(target, 135),
        "winrm": lambda: winrm.check(target, 5985),
        "ldaps": lambda: ldaps.check(target, 636),
        "gc": lambda: gc.check(target, 3268),
        "adws": lambda: adws.check(target, 9389),
        "web": lambda: web.check(target),
        "rdp": lambda: rdp.check(target, 3389),
        "mssql": lambda: mssql.check(target, 1433),
        "adcs": lambda: adcs.check(target),
    }

    with ThreadPoolExecutor(max_workers=8) as executor:

        futures = {
            executor.submit(task): name
            for name, task in tasks.items()
        }

        for future in as_completed(futures):
            service = futures[future]

            try:
                results[service] = future.result()

            except Exception as e:
                results[service] = {
                    "status": "error",
                    "error": str(e)
                }

    success("Escaneo terminado")

    show_report(results)

    if json_output:
        export_json(results)

    if csv_output:
        export_csv(results)

    return results
