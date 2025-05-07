
def run(domain, api_key):
    import requests
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    url = f"https://dns.projectdiscovery.io/dns/{domain}/subdomains"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            results = response.json().get("subdomains", [])
            return [f"{sub}.{domain}" for sub in results]
        else:
            print(f"[!] Chaos API error: {response.status_code}")
            return []
    except Exception as e:
        print(f"[!] Failed to use Chaos plugin: {e}")
        return []
