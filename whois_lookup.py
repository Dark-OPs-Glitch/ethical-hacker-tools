import whois

domain = input("Enter domain: ")

try:
    w = whois.whois(domain)
    
    print("\n--- WHOIS Info ---")
    print(f"Domain: {w.domain_name}")
    print(f"Registrar: {w.registrar}")
    print(f"Created: {w.creation_date}")
    print(f"Expires: {w.expiration_date}")
    print(f"Name Servers: {w.name_servers}")

except Exception as e:
    print("Error:", e)
    print("Make sure you typed domain.com correctly")