import json
import csv

from core.logger import success


def export_json(results, filename="adtool-report.json"):

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    success(f"Reporte JSON guardado en {filename}")


def export_csv(results, filename="adtool-report.csv"):

    with open(filename, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            "Servicio",
            "Estado",
            "Puerto"
        ])

        for service, data in results.items():

            if not data:
                continue

            writer.writerow([
                service.upper(),
                data.get("status", "-"),
                data.get("port", "-")
            ])

    success(f"Reporte CSV guardado en {filename}")
