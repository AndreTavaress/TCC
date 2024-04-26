import threading
import ipaddress
from ping3 import ping
import socket
from .service import scan_ports

from apptcc.models import Dispositivo,Scanner

def check_ip_status(ip):
    response_time = ping(ip, timeout=0.1)
    if response_time is not None:
        return "online"
    else:
        return "offline"

def get_device_name(ip):
    try:
        host = socket.gethostbyaddr(ip)
        return host[0]
    except (socket.herror, socket.gaierror):
        return "Desconhecido"

def process_ip(ip):
    status = check_ip_status(ip)
    device_name = get_device_name(ip)
    print(f"IP: {ip} - Nome do dispositivo: {device_name} - Status: {status}")

    if status.lower() == "online":
        
        teste = Dispositivo.objects.create(
            ip=ip, 
            nome_do_dispositivo=device_name, 
            status=status
            )
        scan_ports(teste)
    else:
        Scanner.objects.create(
            off=ip
        )

def main(target_network, subnet_mask):
#    target_network = input("Digite o endereço de rede (por exemplo, 192.168.0.0): ")
#    subnet_mask = int(input("Digite a máscara de sub-rede (por exemplo, 24): "))
    
    target_block = f"{target_network}/{subnet_mask}"
    ip_network = ipaddress.ip_network(target_block, strict=False)
    
    threads = []

    for ip in ip_network:
        ip_str = str(ip)
        thread = threading.Thread(target=process_ip, args=(ip_str,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
