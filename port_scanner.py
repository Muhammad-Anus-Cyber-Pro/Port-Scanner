# Basic port scanner (Educational)
# Purpose: Network Reconnaissance
# Scope: Authorized & Local network

import socket
from termcolor import colored


# First Function

def scan(ipaddress, max_ports):
    print(colored(f"[*] Starting scan for this {ipaddress}","cyan"))
    
    for port in range(1, max_ports):
        scan_port(ipaddress, port)
    
# Get service banner

def get_banner(sock):
    return sock.recv(1024)

    
# Scan single port

def scan_port(ip, port):
    try:        
        sock = socket.socket()
        sock.settimeout(0.3)
    
        # Try connecting to port
        sock.connect((ip, port))
    
        try:
            banner = get_banner(sock)
            print(colored(f"[+] Port {port} Open : {banner.decode().strip()}","green"))
        except:
            print(colored(f"[+] Port {port} Open","green"))
        
        sock.close()
            
    except:
        # Closed and filtered port
        pass

# ---------------------------
#        Main Program
# ---------------------------

if __name__ == "__main__":
    targets = input("[+] Enter target(s) (comma separated if multiple): ")
    ports = int(input("[+] Enter number of ports to scan: "))
    
    # Multiple targets
    if "," in targets:
        print(colored("\n[+] Multiple targets detected\n","yellow"))
        for target in targets.split(","):
            scan(target,ports)
            
    else:
        scan(targets,ports)
