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

def directory_check(target,dir):
    global result
    
    https_url = f"https://{target}/{dir}"
    http_url = f"http://{target}/{dir}"
    
            
    try:
        r = requests.get(https_url,timeout=2)
                
        if r.status_code < 400:
            print(f"{blue}[+] Found : " + f"{reset}{https_url} : " + f"{green}{r.status_code}")
            result.append(https_url)
                    
    except:
        pass
    try:
        r = requests.get(http_url,timeout=2)
        
        if r.status_code < 400:
            print(f"{blue}[+] Found : " + f"{reset}{http_url} : " + f"{green}{r.status_code}")
            result.append(http_url)
            
    except:
        pass
    return result

def directory_brute(target,dirwordlist,max_threads):
    threads = []
    
    try:
        with open(dirwordlist,"r") as file:
            for line in file:
                dir = line.strip()
            
                while threading.active_count() > max_threads:
                    pass
                
                t = threading.Thread(target=directory_check,args=(target,dir))
                threads.append(t)
                t.start()
                
            for t in threads:
                t.join()
    except FileNotFoundError:
        print(f"{red}[-] File not found: {dirwordlist}")
            