import requests
import threading
from colorama import Fore,init

init(autoreset=True)

red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
reset = Fore.RESET

result = []
lock = threading.Lock()

def check_subdomain(target,sub):
    global result
    
    https_url = f"https://{sub}.{target}"
    http_url = f"http://{sub}.{target}"
    
    try:

        r = requests.get(https_url, timeout=3)

        if r.status_code < 400:
            print(f"{blue}[+] Found : " + f"{reset}{https_url} : " + f"{green}{r.status_code}")
            result.append(https_url)

            return

    except:
        pass

    try:

        r = requests.get(http_url, timeout=3)

        if r.status_code < 400:
            print(f"{blue}[+] Found : " + f"{reset}{http_url} : " + f"{green}{r.status_code}")
            result.append(http_url)

    except:
        pass

def subdomain_find(target,subwordlist,max_threads):
    threads = []
    
    try:
        with open(subwordlist) as file:
            for line in file:
                sub = line.strip()
    
    
                while threading.active_count() > max_threads:
                    pass
                
                t = threading.Thread(target=check_subdomain,args=(target,sub),daemon=True)
                threads.append(t)
                t.start()
                
            for t in threads:
                t.join()
                
        return result
    except FileNotFoundError:
        print(f"{red}[-] File not found: {subwordlist}")