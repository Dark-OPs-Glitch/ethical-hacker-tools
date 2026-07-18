import requests

url = input("Enter website URL: ")
if not url.startswith("http"):
    url = "https://" + url

try:
    response = requests.get(url, timeout=5)
    headers = response.headers
    
    print(f"\n--- Tech Stack for {url} ---")
    
    # Server
    print(f"Server: {headers.get('Server', 'Not found')}")
    
    # CDN / Security
    if 'cloudflare' in str(headers).lower():
        print("CDN: Cloudflare")
    if 'x-powered-by' in headers:
        print(f"Powered by: {headers['X-Powered-By']}")
    
    # Check for common tech in HTML
    html = response.text.lower()
    if 'wp-content' in html:
        print("CMS: WordPress")
    if 'jquery' in html:
        print("JS Library: jQuery")
    if 'react' in html:
        print("Framework: React")
    if 'shopify' in html:
        print("E-commerce: Shopify")
        
    print(f"Status Code: {response.status_code}")
    
except Exception as e:
    print("Error:", e)