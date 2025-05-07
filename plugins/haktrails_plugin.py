
def run(domain, api_key):
    import requests
    headers = {
        "apikey": api_key
    }
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json().get("subdomains", [])
            return [f"{sub}.{domain}" for sub in data]
        else:
            print(f"[!] Haktrails API error: {response.status_code}")
            return []
    except Exception as e:
        print(f"[!] Failed to use Haktrails plugin: {e}")
        return []
