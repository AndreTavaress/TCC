import threading
import ipaddress
from ping3 import ping
import socket
from .service import scan_ports
from django.core.cache import cache


from apptcc.models import Dispositivo

CACHE_KEY_OFFLINE = 'offline_ips'

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
    offline_ips = cache.get(CACHE_KEY_OFFLINE, set())
    status = check_ip_status(ip)
    device_name = get_device_name(ip)
    print(f"IP: {ip} - Nome do dispositivo: {device_name} - Status: {status}")
    
    if not isinstance(ip, set):
        offline_ips = set(ip)
        
    new_off = offline_ips
    if status.lower() == "online":
        
        equipamento = Dispositivo.objects.create(
            ip=ip, 
            nome_do_dispositivo=device_name, 
            status=status
            )
        scan_ports(equipamento)
    else:
        
        offline_ips.update(new_off)
        cache.set(CACHE_KEY_OFFLINE, offline_ips)
        print(offline_ips)

    cache.set(CACHE_KEY_OFFLINE, offline_ips)
def main(target_network, subnet_mask):
    
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
