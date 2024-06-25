import threading
import ipaddress
from ping3 import ping

from apptcc.models import Offline

def check_cidr_block(cidr_block):
    
    Offline.objects.all().delete()
    
    def check_ip_status(ip):
        response_time = ping(ip, timeout=0.1)
        if response_time is not None:
            return "online"
        else:
            return "offline"

    def process_ip(ip):
        status = check_ip_status(ip)
        if status == 'offline':
            Offline.objects.create(
                bloco = cidr_block,
                ip = ip
            )

    ip_network = ipaddress.ip_network(cidr_block, strict=False)
    threads = []

    for ip in ip_network:
        ip_str = str(ip)
        thread = threading.Thread(target=process_ip, args=(ip_str,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    