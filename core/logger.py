from rich.console import Console

console = Console()


def info(message):
    console.print(f"[bold cyan][*][/bold cyan] {message}")


def success(message):
    console.print(f"[bold green][+][/bold green] {message}")


def warning(message):
    console.print(f"[bold yellow][!][/bold yellow] {message}")


def error(message):
    console.print(f"[bold red][-][/bold red] {message}")


def critical(message):
    console.print(f"[bold white on red][CRITICAL][/bold white on red] {message}")
