
import os
import subprocess
import platform
import shutil
from datetime import datetime

LOG_FILE = "hybrid_sub.log"
REQUIRED_TOOLS = ["subfinder", "amass", "puredns", "dnsx", "shuffledns", "assetfinder", "findomain"]

def log_message(message):
    with open(LOG_FILE, "a") as log:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log.write(f"{timestamp} {message}\n")

def check_required_tools():
    print("[*] Checking for required tools...")
    missing = []
    for tool in REQUIRED_TOOLS:
        if shutil.which(tool) is None:
            print(f"[!] Missing tool: {tool}")
            log_message(f"Missing tool: {tool}")
            missing.append(tool)
        else:
            print(f"[+] Found: {tool}")
    return missing

def try_auto_install(tool):
    print(f"[~] Attempting auto-install for {tool}")
    install_cmds = {
        "subfinder": "go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
        "amass": "go install -v github.com/owasp-amass/amass/v3/...@master",
        "puredns": "go install github.com/d3mondev/puredns/v2@latest",
        "shuffledns": "go install -v github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest",
        "dnsx": "go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest",
        "assetfinder": "go install github.com/tomnomnom/assetfinder@latest",
        "findomain": "curl -LO https://github.com/Findomain/Findomain/releases/latest/download/findomain.exe && move findomain.exe C:\\Windows\\System32"
    }
    cmd = install_cmds.get(tool)
    if cmd:
        try:
            subprocess.run(cmd, shell=True)
            log_message(f"Auto-install attempted for {tool}")
        except Exception as e:
            print(f"[!] Failed to install {tool}: {e}")
            log_message(f"Install failed for {tool}: {e}")
    else:
        print(f"[!] No install command configured for {tool}")
        log_message(f"No install command configured for {tool}")

def main():
    print("Hybrid_Sub Launcher")
    print("[*] Logging to hybrid_sub.log")
    log_message("Launcher started")

    missing = check_required_tools()
    if missing:
        print("\n[!] The following tools are missing:")
        for tool in missing:
            print(f"    - {tool}")
        print("\n[*] Attempting auto-install...")
        for tool in missing:
            try_auto_install(tool)

        print("\n[*] Rechecking after auto-install...")
        missing_after = check_required_tools()
        if missing_after:
            print("\n[!] Some tools are still missing. Please install them manually.")
            log_message("Manual installation required for: " + ", ".join(missing_after))
            return

    print("\n[1] Run Python Version")
    print("[2] Run Go Version")
    choice = input("Select an option: ")

    if choice == "1":
        subprocess.run(["python", "python_core/main.py"])
    elif choice == "2":
        os_type = platform.system().lower()
        if os_type == "windows":
            subprocess.run(["go", "run", "go_core/main.go"], shell=True)
        else:
            subprocess.run(["go", "run", "go_core/main.go"])
    else:
        print("Invalid option.")

    log_message("Launcher completed")

if __name__ == "__main__":
    main()
