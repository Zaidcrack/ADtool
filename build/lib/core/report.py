from rich.table import Table
from rich.console import Console

console = Console()


def show_report(results):

    table = Table(title="ADtool Scan Report")

    table.add_column("Servicio")
    table.add_column("Estado")
    table.add_column("Detalles")

    for service, data in results.items():

        if not data:
            status = "error"
            details = "-"
        else:
            status = data.get("status", "checked")

            if service == "kerberos":
                details = (
                    f"TCP: {'OPEN' if data['tcp'] else 'CLOSED'} | "
                    f"UDP: {'OPEN' if data['udp'] else 'CLOSED'}"
                )

            elif service == "dns":
                details = f"Puerto {data['port']}"

            else:
                details = f"Puerto {data['port']}"

        table.add_row(
            service.upper(),
            status,
            details
        )

    console.print(table)
