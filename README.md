# ADtool

Herramienta de enumeración para **Active Directory** desarrollada en **Python**, diseñada para facilitar la identificación y análisis de servicios comunes en entornos Windows.

## Características

- Enumeración SMB
- Enumeración LDAP
- Detección de LDAPS
- Detección de Kerberos
- Enumeración DNS
- Enumeración RPC
- Detección de WinRM
- Detección de Global Catalog
- Detección de Active Directory Web Services (ADWS)
- Escaneo completo de Active Directory

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Zaidcrack/ADtoolkit.git
cd ADtoolkit
```

Instalar con **pipx**:

```bash
pipx install .
```

O instalar con **pip**:

```bash
pip install .
```

## Uso

Mostrar la ayuda:

```bash
adtool --help
```

Escaneo completo:

```bash
adtool scan <IP>
```

Ejemplos:

```bash
adtool smb 10.10.10.10
adtool ldap 10.10.10.10
adtool kerberos 10.10.10.10
adtool dns 10.10.10.10 --domain thm.local
adtool rpc 10.10.10.10
adtool winrm 10.10.10.10
adtool gc 10.10.10.10
adtool adws 10.10.10.10
```

## Requisitos

- Python 3.10 o superior
- Impacket
- ldap3
- dnspython
- Rich
- Typer
- Cryptography

## Hoja de ruta

### Implementado ✅

- [x] SMB
- [x] LDAP
- [x] Kerberos
- [x] DNS
- [x] RPC
- [x] WinRM
- [x] LDAPS
- [x] Global Catalog
- [x] Active Directory Web Services
- [x] Escaneo completo

### Próximamente 🚧

- [ ] Enumeración de usuarios
- [ ] Enumeración de grupos
- [ ] Enumeración de equipos
- [ ] Enumeración de recursos compartidos
- [ ] Enumeración de GPO
- [ ] Enumeración de relaciones de confianza (Trusts)
- [ ] Política de contraseñas
- [ ] RID Bruteforce
- [ ] AS-REP Roasting
- [ ] Kerberoasting
- [ ] BloodHound Export
- [ ] Enumeración de AD CS
- [ ] Soporte para autenticación con credenciales

## Licencia

Este proyecto está distribuido bajo la licencia **MIT**.

## Autor

Desarrollado por **Zaidcrack**.
