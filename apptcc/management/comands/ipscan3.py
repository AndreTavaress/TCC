import threading
import socket
import ipaddress

def scan_ip(ip):
    try:
        host = socket.gethostbyaddr(ip)
        print(f"IP: {ip} - Nome do dispositivo: {host[0]}")
    except (socket.herror, socket.gaierror):
        print(f"IP: {ip} - Nome do dispositivo: Desconhecido")

def main():
    target_network = input("Digite o endereço de rede (por exemplo, 192.168.0.0/24): ")
    
    ip_network = ipaddress.ip_network(target_network, strict=False)
    threads = []

    for ip in ip_network:
        ip_str = str(ip)
        thread = threading.Thread(target=scan_ip, args=(ip_str,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
