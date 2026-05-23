import socket
import threading
from colorama import Fore,init

init(autoreset=True)

blue = Fore.BLUE
reset = Fore.RESET

open_ports = []
lock = threading.Lock()

def check_port(target, port):
    global lock
    global open_ports
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        with lock:
            print(f"{blue}[+] Port " + f"{reset}{port}" + f"{blue} is open")
        open_ports.append(port)

    s.close()
    


def port_scan(target, ports, max_threads):
    global open_ports
    
    try:
        target = socket.gethostbyname(target)
    except:
        pass

    if "-" in ports:
        start, end = map(int, ports.split("-"))
        port_list = range(start, end + 1)

    else:
        port_list = [int(p) for p in ports.split(",")]

    threads = []

    for port in port_list:

        while threading.active_count() >= max_threads:
            pass

        t = threading.Thread(target=check_port,args=(target, port),daemon=True)

        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    return open_ports
    