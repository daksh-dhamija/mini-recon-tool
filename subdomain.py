import requests
import threading

result = []
lock = threading.Lock()

def check_subdomain(target,sub):
    global result
    

    url = f"http://{sub}.{target}"
            
    try:
        r = requests.get(url, timeout=3)
                
        if r.status_code < 400:
            print(f"[+]Found {url} : {r.status_code}")
            result.append(url)
    except:
        pass
    return result

def subdomain_find(target,subwordlist,max_threads):
    threads = []
    
    try:
        with open(subwordlist) as file:
            for line in file:
                sub = line.strip()
    
    
                while threading.active_count() > max_threads:
                    pass
                
                t = threading.Thread(target=check_subdomain,args=(target,sub))
                threads.append(t)
                t.start()
                
            for t in threads:
                t.join()
                
        return result
    except FileNotFoundError:
        print(f"[-] File not found: {subwordlist}")