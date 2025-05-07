import shutil

import os
import subprocess
import threading
from plugin_runner import run_plugins
from datetime import datetime

LOG_FILE = "hybrid_sub_scan.log"
THREADS = 5  # Number of concurrent domain scans

def log_message(message):
    with open(LOG_FILE, "a") as log:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log.write(f"{timestamp} {message}\n")

def run_passive_enum(domain):
    try:
        print(f"[+] Running passive enumeration for {domain}")
        os.system(f"subfinder -d {domain} -silent -o tmp_{domain}_passive.txt")
        os.system(f"assetfinder --subs-only {domain} >> tmp_{domain}_passive.txt")
        log_message(f"Passive enumeration completed for {domain}")
    except Exception as e:
        print(f"[!] Passive enumeration failed: {e}")
        log_message(f"Error in passive enumeration for {domain}: {e}")


def run_active_enum(domain):
    try:
        if shutil.which("massdns"):
            print(f"[+] Running active bruteforce with puredns for {domain}")
            os.system(f"puredns bruteforce wordlists/dns.txt {domain} -r resolvers.txt > tmp_{domain}_active.txt")
            log_message(f"Active enumeration completed for {domain}")
        else:
            msg = f"massdns not found. Skipping active bruteforce for {domain}"
            print(f"[!] " + msg)
            log_message(f"[WARNING] {msg}")
            with open(f"tmp_{domain}_active.txt", "w") as f:
                f.write("")  # Create empty file to allow combine step
    except Exception as e:
        print(f"[!] Active enumeration failed: {e}")
        log_message(f"Error in active enumeration for {domain}: {e}")
def combine_results(domain, plugin_subs):
    try:
        with open(f"tmp_{domain}_passive.txt") as f1, open(f"tmp_{domain}_active.txt") as f2:
            all_subs = set(f1.read().splitlines() + f2.read().splitlines() + plugin_subs)
        with open(f"results_{domain}.txt", "w") as fout:
            for sub in sorted(all_subs):
                fout.write(sub + "\n")
        print(f"[+] Results saved to results_{domain}.txt")
        log_message(f"Subdomain results saved for {domain}")
    except Exception as e:
        print(f"[!] Failed to combine results: {e}")
        log_message(f"Error combining results for {domain}: {e}")

def scan_domain(domain):
    log_message(f"Scan started for domain: {domain}")
    run_passive_enum(domain)
    run_active_enum(domain)

    try:
        plugin_subs = run_plugins(domain)
        log_message(f"Plugin enumeration completed for {domain} with {len(plugin_subs)} subs")
    except Exception as e:
        plugin_subs = []
        print(f"[!] Plugin runner failed for {domain}: {e}")
        log_message(f"Plugin runner error for {domain}: {e}")

    combine_results(domain, plugin_subs)
    log_message(f"Scan completed for domain: {domain}")

def main():
    print("Hybrid_Sub - Multi-target Scanner")
    file_input = input("Enter single domain or path to file with targets: ").strip()

    if os.path.isfile(file_input):
        with open(file_input) as f:
            domains = [line.strip() for line in f if line.strip()]
    else:
        domains = [file_input]

    threads = []
    for domain in domains:
        while threading.active_count() > THREADS:
            pass  # Wait for a thread slot
        t = threading.Thread(target=scan_domain, args=(domain,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("[*] All scans complete.")

if __name__ == "__main__":
    main()
