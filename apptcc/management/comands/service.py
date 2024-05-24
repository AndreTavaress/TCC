import socket

from apptcc.models import Service

def scan_ports(ip):
    target_ip = ip
    active_services = []

    service_ports = {

        1: "TCPmux",
        2: "CompressNET Management Utility",
        3: "CompressNET Compression Process",
        4: "CompressNET Compression Control",
        5: "Remote Job Entry",
        6: "Unassigned",
        7: "Echo Protocol",
        9: "Discard Protocol",
        13: "Daytime Protocol",
        17: "QOTD",
        19: "Chargen",
        20: "FTP - Data",
        21: "FTP - Control",
        22: "SSH",
        23: "Telnet",
        25: "SMTP ",
        37: "Time Protocol",
        43: "Whois Protocol",
        53: "DNS",
        67: "DHCP",
        69: "TFTP",
        80: "HTTP",
        88: "Kerberos",
        110: "POP3",
        119: "NNTP",
        123: "NTP",
        137: "NetBIOS Name Service",
        138: "NetBIOS Datagram Service",
        139: "NetBIOS Session Service",
        143: "IMAP",
        161: "SNMP",
        389: "LDAP",
        443: "HTTPS",
        445: "SMB",
        636: "LDAPS",
        389: "Microsoft-DS Active Directory",
        465: "SMTPS",
        993: "IMAPS",
        995: "POP3S",
        1433: "Microsoft SQL Server",
        3306: "MySQL Database",
        5432: "PostgreSQL Database",
        3389: "(RDP)",
        9418: "Git",
        27017: "MongoDB",
        6379: "Redis",
        9200: "Elasticsearch",
        11211: "Memcached",
        1521: "Oracle Database",
        1433: "Microsoft SQL Server",
        990: "FTP - SSL",
        587: "SMTP Submission",
        8080: "HTTP Alternate",
        993: "IMAP Alternate",
        995: "POP3 Alternate",
        1186: "MySQL Cluster",
        3128: "HTTP Proxy",
        6667: "IRC",
        3268: "Microsoft Exchange",
    }

    try:
        for port, service in service_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1) 
            result = sock.connect_ex((target_ip.ip, port))
            if result == 0:
                active_services.append((port, service))
                
            sock.close()

    except socket.gaierror:
        print(f'Erro de resolução de host para {target_ip}')
    except socket.error:
        print(f'Não foi possível conectar-se a {target_ip}')
    
    linhas = [f"{item[1]}" for item in active_services]
    texto = " - ".join(linhas)
    Service.objects.create(
        dispositivo=target_ip, 
        lista_de_coisas=texto
    )
    return active_services


if __name__ == "__main__":
    scan_ports()

