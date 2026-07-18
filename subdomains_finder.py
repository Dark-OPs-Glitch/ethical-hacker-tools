import requests

domain = input("Enter domain without https:// : ")

subdomains = ["www", "mail", "ftp", "admin", "test", "dev", "api", "blog", "shop", "portal"]

print(f"\nScanning subdomains for {domain}...")

for sub in subdomains:
    url = f"https://{sub}.{domain}"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code < 400:
            print(f"[+] Found: {url}")
    except:
        pass

print("\nScan complete!")