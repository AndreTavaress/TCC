import threading
import ipaddress
from ping3 import ping

def ping_ip(ip):
    for _ in range(1):
        response_time = ping(ip, timeout=0.1)
        if response_time is not None:
            print(f"IP {ip} está online (Tempo de resposta: {response_time} ms)")
            break
        else:
            print(f"IP {ip} está offline")

def main():
    target_network = input("Digite o endereço de rede (por exemplo, 192.168.0.0): ")
    subnet_mask = int(input("Digite a máscara de sub-rede (por exemplo, 24): "))
    
    target_block = f"{target_network}/{subnet_mask}"
    ip_network = ipaddress.ip_network(target_block, strict=False)
    
    thread_list = []

    for ip in ip_network:
        ip_str = str(ip)
        thread = threading.Thread(target=ping_ip, args=(ip_str,))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    main()
