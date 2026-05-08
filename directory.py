import requests
import threading

result = []
lock = threading.Lock()

def directory_check(target,dir):
    global result
    
    
    url = f"http://{target}/{dir}"
            
    try:
        r = requests.get(url)
                
        if r.status_code < 400:
            print(f"Found {url} : {r.status_code}")
            result.append(url)
                    
    except:
        pass
    return result

def directory_brute(target,dirwordlist,max_threads):
    threads = []
    
    try:
        with open(dirwordlist,"r") as file:
            for line in file:
                dir = line.strip()
            
                while threading.active_count() < max_threads:
                    pass
                
                t = threading.Thread(target=directory_check,args=(target,dir))
                threads.append(t)
                t.start()
                
            for t in threads:
                t.join()
    except FileNotFoundError:
        print(f"[-] File not found: {dirwordlist}")
            