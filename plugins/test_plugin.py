
def run(domain, api_key):
    print(f"[TestPlugin] Running custom plugin logic for {domain}")
    # Simulate discovery of dummy subdomains
    return [f"test1.{domain}", f"test2.{domain}"]
