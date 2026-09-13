import typer

from AD.plugins import smb as smb_module
from AD.plugins import ldap as ldap_module
from AD.plugins import kerberos as kerberos_module
from core.banner import show
from core.config import NAME, VERSION
from AD.plugins import dns as dns_module
from AD.plugins import scan as scan_module
from AD.plugins import rpc as rpc_module
from AD.plugins import winrm as winrm_module
from AD.plugins import gc as gc_module
from AD.plugins import adws as adws_module
from AD.plugins import domain as domain_module
from AD.plugins import web as web_module
from AD.plugins import rdp as rdp_module
from AD.plugins import mssql as mssql_module
from AD.plugins import adcs as adcs_module

app = typer.Typer(
    name="adtool",
    help="ADtool - Active Directory Toolkit"
)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Punto de entrada principal de ADtool.
    """
    if ctx.invoked_subcommand is None:
        show()
        typer.echo(f"{NAME} v{VERSION}")
        typer.echo("Usa 'adtool --help' para ver los comandos disponibles.")


@app.command()
def smb(
    target: str,
    port: int = typer.Option(445, "--port", "-p"),
    timeout: int = typer.Option(3, "--timeout", "-t"),
    username: str = typer.Option("", "--username", "-u"),
    password: str = typer.Option("", "--password", "-P"),
    domain: str = typer.Option("", "--domain", "-d"),
    hashes: str = typer.Option("", "--hashes", "-H"),
    kerberos: bool = typer.Option(False, "--kerberos", "-k"),
):
    """
    Comprobación y análisis del servicio SMB.
    """
    smb_module.check(
        target,
        port,
        timeout,
        username,
        password,
        domain,
        hashes,
        kerberos
    )

@app.command()
def ldap(
    target: str,
    port: int = typer.Option(389, "--port", "-p")
):
    """
    Enumeración de información mediante LDAP.
    """
    ldap_module.enum(target, port)


@app.command()
def kerberos(
    domain: str,
    port: int = typer.Option(88, "--port", "-p")
):
    """
    Comprobación de configuración Kerberos.
    """
    kerberos_module.check(domain, port)


@app.command()
def version():
    """
    Muestra la versión de ADtool.
    """
    typer.echo(f"{NAME} v{VERSION}")
@app.command()
def scan(
    target: str
):
    """
    Escaneo completo de servicios Active Directory.
    """
    scan_module.run(target)

@app.command()
def rpc(
    target: str,
    port: int = typer.Option(135, "--port", "-p")
):
    """
    Enumeración RPC.
    """
    rpc_module.check(target, port)


@app.command()
def winrm(
    target: str,
    port: int = typer.Option(5985, "--port", "-p")
):
    """
    Enumeración WinRM.
    """
    winrm_module.check(target, port)

@app.command()
def gc(
    target: str,
    port: int = typer.Option(3268, "--port", "-p")
):
    """
    Enumeración Global Catalog.
    """
    gc_module.check(target, port)

@app.command()
def adws(
    target: str,
    port: int = typer.Option(9389, "--port", "-p")
):
    """
    Enumeración Active Directory Web Services.
    """
    adws_module.check(target, port)
@app.command()
def dns(
    target: str,
    port: int = typer.Option(53, "--port", "-p"),
    domain: str = typer.Option(None, "--domain", "-d")
):
    """
    Enumeración DNS.
    """
    dns_module.enum(target, port, domain)

@app.command()
def domain(
    target: str,
    port: int = typer.Option(389, "--port", "-p")
):
    """
    Enumeración del dominio Active Directory.
    """
    domain_module.enum(target, port)

@app.command()
def web(
    target: str
):
    """
    Enumeración Web.
    """
    web_module.check(target)


@app.command()
def rdp(
    target: str,
    port: int = typer.Option(3389, "--port", "-p")
):
    """
    Enumeración RDP.
    """
    rdp_module.check(target, port)


@app.command()
def mssql(
    target: str,
    port: int = typer.Option(1433, "--port", "-p")
):
    """
    Enumeración MSSQL.
    """
    mssql_module.check(target, port)


@app.command()
def adcs(
    target: str
):
    """
    Enumeración Active Directory Certificate Services.
    """
    adcs_module.check(target)

@app.command()
def scan(
    target: str,
    json_output: bool = typer.Option(False, "--json"),
    csv_output: bool = typer.Option(False, "--csv")
):
    """
    Escaneo completo de servicios Active Directory.
    """
    scan_module.run(target, json_output, csv_output)


if __name__ == "__main__":
    app()
