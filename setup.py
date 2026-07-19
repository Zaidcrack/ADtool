from setuptools import setup, find_packages

setup(
    name="ADtool",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "impacket",
        "ldap3",
        "pyasn1",
        "pyOpenSSL",
        "cryptography",
        "scapy",
        "rich",
        "typer",
        "tabulate",
        "requests",
        "colorama",
        "pyfiglet",
        "dnspython"
    ],
    entry_points={
        "console_scripts": [
            "adtool=AD.cli:app"
        ]
    }
)
