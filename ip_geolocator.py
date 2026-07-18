import requests

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'fail':
        print("Invalid IP or Domain")
        return
    
    print("\n--- IP Location Info ---")
    print(f"IP Address : {data['query']}")
    print(f"Country    : {data['country']}")
    print(f"Region     : {data['regionName']}")
    print(f"City       : {data['city']}")
    print(f"ZIP        : {data['zip']}")
    print(f"ISP        : {data['isp']}")
    print(f"Org        : {data['org']}")
    print(f"Lat/Long   : {data['lat']}, {data['lon']}")
    print(f"Timezone   : {data['timezone']}")

ip = input("Enter IP address: ")
get_ip_info(ip)