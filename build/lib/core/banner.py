from pyfiglet import Figlet
from rich.console import Console

console = Console()


def show():
    fig = Figlet(font="slant")

    banner = fig.renderText("ADtool")

    console.print(
        f"[bold cyan]{banner}[/bold cyan]"
    )

    console.print("[bold green]Active Directory Toolkit[/bold green]")
    console.print("[yellow]Version 0.1[/yellow]\n")
