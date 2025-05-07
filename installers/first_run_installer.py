
import os
import subprocess
import platform
import shutil
import sys

try:
    from colorama import init, Fore, Style
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import init, Fore, Style

init(autoreset=True)

GO_TOOLS = {
    'subfinder': 'go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest',
    'amass': 'go install -v github.com/owasp-amass/amass/v3/...@master',
    'puredns': 'go install github.com/d3mondev/puredns/v2@latest',
    'shuffledns': 'go install -v github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest',
    'dnsx': 'go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest',
    'assetfinder': 'go install github.com/tomnomnom/assetfinder@latest'
}

WINDOWS_ONLY = {
    'findomain': 'curl -LO https://github.com/Findomain/Findomain/releases/latest/download/findomain.exe && move findomain.exe C:\\Windows\\System32'
}

PYTHON_MODULES = [
    'requests'
]

def check_command(cmd):
    return shutil.which(cmd) is not None

def install_python_packages():
    print(Fore.CYAN + "[*] Installing required Python modules...")
    for module in PYTHON_MODULES:
        try:
            __import__(module)
            print(Fore.GREEN + f"[+] Python module found: {module}")
        except ImportError:
            print(Fore.YELLOW + f"[!] Installing Python module: {module}")
            subprocess.run([sys.executable, "-m", "pip", "install", module])

def is_tool_installed(tool):
    return shutil.which(tool) is not None

def install_tool(tool, command, os_type):
    print(Fore.YELLOW + f"[+] Installing {tool}...")
    if os_type == "windows":
        subprocess.run(command, shell=True)
    else:
        subprocess.run(command, shell=True, executable='/bin/bash')

def check_environment():
    print(Fore.CYAN + "[*] Checking environment...")

    # Check Python
    print(Fore.CYAN + "[*] Checking Python...")
    try:
        print(Fore.GREEN + f"[+] Python Version: {sys.version}")
    except Exception as e:
        print(Fore.RED + f"[!] Python not found: {e}")
        sys.exit(1)

    # Check pip
    print(Fore.CYAN + "[*] Checking pip...")
    if not check_command("pip"):
        print(Fore.RED + "[!] pip is not installed. Please install pip before proceeding.")
        sys.exit(1)
    else:
        print(Fore.GREEN + "[+] pip is installed.")

    # Check Go
    print(Fore.CYAN + "[*] Checking Go...")
    if not check_command("go"):
        print(Fore.RED + "[!] Go is not installed or not in PATH. Please install Go from https://go.dev/")
        sys.exit(1)
    else:
        result = subprocess.run(["go", "version"], stdout=subprocess.PIPE)
        print(Fore.GREEN + f"[+] {result.stdout.decode().strip()}")

def main():
    flag_file = os.path.expanduser("~/.hybrid_sub_initialized")
    if os.path.exists(flag_file):
        print(Fore.GREEN + "[*] Tools already installed. Skipping installation.")
        return

    os_type = platform.system().lower()
    print(Fore.CYAN + f"[*] Detected OS: {os_type}")

    check_environment()
    install_python_packages()

    for tool, command in GO_TOOLS.items():
        if not is_tool_installed(tool):
            install_tool(tool, command, os_type)
        else:
            print(Fore.GREEN + f"[+] {tool} is already installed.")

    if os_type == 'windows':
        for tool, command in WINDOWS_ONLY.items():
            if not is_tool_installed(tool):
                install_tool(tool, command, os_type)

    with open(flag_file, 'w') as f:
        f.write("installed")

    print(Fore.GREEN + "[*] Setup complete.")

if __name__ == "__main__":
    main()
