import socket

from apptcc.models import Service

def scan_ports(ip):
    target_ip = ip
    active_services = []

    service_ports = {

        1: "TCPmux (TCP Port Service Multiplexer)",
        2: "CompressNET Management Utility",
        3: "CompressNET Compression Process",
        4: "CompressNET Compression Control",
        5: "Remote Job Entry",
        6: "Unassigned",
        7: "Echo Protocol",
        9: "Discard Protocol",
        13: "Daytime Protocol",
        17: "QOTD (Quote of the Day)",
        19: "Chargen (Character Generator)",
        20: "FTP (File Transfer Protocol) - Data",
        21: "FTP (File Transfer Protocol) - Control",
        22: "SSH (Secure Shell)",
        23: "Telnet",
        25: "SMTP (Simple Mail Transfer Protocol)",
        37: "Time Protocol",
        43: "Whois Protocol",
        53: "Domain Name System (DNS)",
        67: "DHCP (Dynamic Host Configuration Protocol)",
        69: "TFTP (Trivial File Transfer Protocol)",
        80: "HTTP (Hypertext Transfer Protocol)",
        88: "Kerberos",
        110: "POP3 (Post Office Protocol version 3)",
        119: "NNTP (Network News Transfer Protocol)",
        123: "NTP (Network Time Protocol)",
        137: "NetBIOS Name Service",
        138: "NetBIOS Datagram Service",
        139: "NetBIOS Session Service",
        143: "IMAP (Internet Message Access Protocol)",
        161: "SNMP (Simple Network Management Protocol)",
        389: "LDAP (Lightweight Directory Access Protocol)",
        443: "HTTPS (Hypertext Transfer Protocol Secure)",
        445: "SMB (Server Message Block)",
        636: "LDAPS (LDAP over SSL)",
        389: "Microsoft-DS Active Directory",
        465: "SMTPS (SMTP Secure)",
        993: "IMAPS (IMAP Secure)",
        995: "POP3S (POP3 Secure)",
        1433: "Microsoft SQL Server",
        3306: "MySQL Database",
        5432: "PostgreSQL Database",
        3389: "Remote Desktop Protocol (RDP)",
        9418: "Git",
        27017: "MongoDB",
        6379: "Redis",
        9200: "Elasticsearch",
        11211: "Memcached",
        1521: "Oracle Database",
        1433: "Microsoft SQL Server",
        990: "FTP - SSL",
        587: "SMTP Submission (Mail Submission Agent)",
        8080: "HTTP Alternate",
        993: "IMAP Alternate",
        995: "POP3 Alternate",
        1186: "MySQL Cluster",
        3128: "HTTP Proxy",
        6667: "IRC (Internet Relay Chat)",
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
    
    linhas = [f"{item[0]}" for item in active_services]
    texto = " - ".join(linhas)
    Service.objects.create(
        dispositivo=target_ip, 
        lista_de_coisas=texto
    )
    return active_services


if __name__ == "__main__":
    scan_ports()

