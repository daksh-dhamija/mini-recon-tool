import argparse
from subdomain import subdomain_find
from directory import directory_brute
from portscan import port_scan

def main():
    print("""
================================================
                MINI RECON TOOL
================================================
Modules:
[1] Subdomain Scan
[2] Directory Bruteforce
[3] Port Scan
================================================
""")
    
    parser = argparse.ArgumentParser(description = "This  is a mini recon tool that can do subdomain scanning, directory bruteforcing, port scanning",usage = "python3 main.py [-t, --target] [-sw, --subwordlist] [-dw, --dirwordlist] [-p, --ports] [-o, --output]")
    parser.add_argument("-sw","--subwordlist",help ="Enter subdomain wordlist")
    parser.add_argument("-dw","--dirwordlist",help ="Enter directory wordlist")
    parser.add_argument("-t","--target",help ="Enter Target[Domain or IP]")
    parser.add_argument("-p","--ports",help ="Enter ports(range = 10-100) or (10,21,22,80)")
    parser.add_argument("-th","--threads",type=int,default=20,help ="Enter threads for speed")
    parser.add_argument("-o","--output",help ="Enter filename for writing output")

    args = parser.parse_args()
    
    subwordlist = args.subwordlist
    dirwordlist = args.dirwordlist
    target = args.target
    ports = args.ports
    threads = args.threads
    output = args.output
    
    if not target:
        print("[-] Please provide target")
        return
    
    if subwordlist:
        print(f"\n[+] Subdomain scan:")
        subs = subdomain_find(target,subwordlist,threads)
        if output:
            with open(output,"a")as file:
                file.write("\n[+] Subdomains found:\n")
                for sub in subs:
                    file.write(sub + "\n")
        
        
    if dirwordlist:
        print(f"\n[+] Directory scan:")
        dirs = directory_brute(target,dirwordlist,threads)
        if output:
            with open(output,"a")as file:
                file.write("\n[+] Directories found:\n")
                for directory in dirs:
                    file.write(directory + "\n")
        
    if ports:
        print(f"\n[+] Port scan:")
        open_ports = port_scan(target,ports,threads)
        if output:
            with open(output,"a")as file:
                file.write("\n[+] Ports found:\n")
                for port in open_ports:
                    file.write(f"Port {port} is open\n")

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\n[!] Program interrupted by user")
