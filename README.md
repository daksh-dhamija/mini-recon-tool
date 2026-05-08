# Mini Recon Tool 🛡️

A powerful, beginner-friendly Python-based reconnaissance tool designed for automated security testing and information gathering. This tool streamlines the initial phase of penetration testing by combining subdomain discovery, directory brute-forcing, and port scanning into a single, multithreaded workflow.

## 🚀 Features

* **Subdomain Enumeration:** Identify subdomains using customizable wordlists.
* **Directory Brute Forcing:** Discover hidden paths and files on web servers.
* **Port Scanning:** Fast TCP port scanning to identify open services.
* **Multithreading:** Built for high-speed performance to handle concurrent tasks.
* **Output Saving:** Save all discovered data to a file for further analysis.

## 🛠️ Built With

* **Python 3**
* **Requests Library:** For handling HTTP requests and status codes.
* **Socket Module:** For network communication and port identification.
* **Threading:** To ensure fast execution of recon tasks.

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/daksh-dhamija/mini-recon-tool.git

## ⚡ Usage

### Subdomain Scan

```bash
python main.py -t example.com -sw subdomains.txt
```

### Directory Bruteforce

```bash
python main.py -t example.com -dw directories.txt
```

### Port Scan

```bash
python main.py -t 192.168.1.1 -p 20-100
```

### Save Output

```bash
python main.py -t example.com -sw subdomains.txt -o output.txt
```

## ⚠️ Disclaimer

This project is intended for educational and authorized security testing purposes only.