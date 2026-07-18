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


## ⚠️ Descargo de responsabilidad

ADtool ha sido desarrollado con fines educativos, de investigación y para realizar auditorías de seguridad autorizadas.

El uso de esta herramienta contra sistemas o redes sin autorización expresa puede ser ilegal y constituir un delito en algunas jurisdicciones.

El autor no se hace responsable del uso indebido, daños, pérdidas o consecuencias derivadas del uso de este software.

Al utilizar ADtool, el usuario acepta que es el único responsable de cumplir con las leyes y regulaciones aplicables en su país.

## ⚠️ Aviso legal

ADtool está destinado exclusivamente para pruebas de penetración autorizadas, laboratorios de aprendizaje y fines de investigación.

No utilice esta herramienta contra sistemas para los que no tenga autorización explícita.

El autor no asume ninguna responsabilidad por el uso indebido de este software, incluyendo actividades ilegales o daños ocasionados a terceros.

Si trabaja para organismos gubernamentales, militares, de inteligencia o cualquier otra organización, asegúrese de contar con la autorización correspondiente antes de utilizar esta herramienta.

