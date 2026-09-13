from core.logger import info, success, warning, error
from core.network import check_tcp

import dns.resolver


def enum(target, port, domain=None):
    info(f"Objetivo DNS: {target}")
    info(f"Puerto: {port}")

    try:
        dns_status = check_tcp(target, port)

        if not dns_status:
            warning(f"DNS no disponible en puerto {port}")

            return {
                "target": target,
                "port": port,
                "protocol": "DNS",
                "status": "offline"
            }

        success(f"DNS disponible en puerto {port}")

        results = {
            "target": target,
            "port": port,
            "protocol": "DNS",
            "status": "online"
        }

        if domain is None:
            return results

        info(f"Buscando registros SRV para {domain}")

        resolver = dns.resolver.Resolver()
        resolver.nameservers = [target]

        srv_records = {
        "LDAP": f"_ldap._tcp.dc._msdcs.{domain}",
        "KERBEROS_TCP": f"_kerberos._tcp.{domain}",
        "KERBEROS_UDP": f"_kerberos._udp.{domain}",
        "GC": f"_gc._tcp.{domain}",
        "KPASSWD_TCP": f"_kpasswd._tcp.{domain}",
        "KPASSWD_UDP": f"_kpasswd._udp.{domain}",
        "PDC": f"_ldap._tcp.pdc._msdcs.{domain}"
}
        results["srv"] = {}

        for service, record in srv_records.items():
            try:
                answers = resolver.resolve(record, "SRV")

                results["srv"][service] = []

                for r in answers:
                    success(
                        f"{service}: {r.target}:{r.port} "
                        f"(prio={r.priority}, weight={r.weight})"
                    )

                    results["srv"][service].append({
                        "host": str(r.target).rstrip("."),
                        "port": r.port,
                        "priority": r.priority,
                        "weight": r.weight
                    })

            except Exception:
                warning(f"No se encontraron registros {service}")

        return results

    except Exception as e:
        error(f"DNS error: {e}")
        return None
