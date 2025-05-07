
# 🚀 Hybrid_Sub – Elite Subdomain Enumeration Framework

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Go](https://img.shields.io/badge/go-1.20+-lightblue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-green)
![License](https://img.shields.io/badge/license-MIT-brightgreen)

> Developed by **SecOpsElite** – For professional bug bounty hunters, red teamers, and ethical hackers.

---

## 🧠 What is Hybrid_Sub?

**Hybrid_Sub** is a high-performance subdomain enumeration tool built with **Python & Go**, designed to combine the strength of **active, passive, and wildcard-aware scanning**.

Key Features:
- 🔎 Passive Enum: APIs (Chaos, Shodan, SecurityTrails), CT logs
- ⚔️ Active Brute-force: Wordlist fuzzing via Puredns & MassDNS
- 🎛 Plugin System: Easily extendable, API-capable
- 🎯 Optimized for speed, accuracy, and extensibility

---

## 🛠 OS Support & Setup

### ✅ Windows 10/11
1. Install [Go](https://go.dev/dl/) and ensure it's in PATH
2. Install [Python 3.10+](https://www.python.org/downloads/windows/)
3. Clone this repo:
   ```powershell
   git clone https://github.com/SecOpsElite/Hybrid_Sub.git
   cd Hybrid_Sub
   ```
4. Run the installer:
   ```powershell
   python installers/first_run_installer.py
   ```
5. For `massdns`, run:
   ```powershell
   installers\setup_massdns_windows.bat
   ```

---

### ✅ Ubuntu / Debian (Linux)
```bash
sudo apt update && sudo apt install -y golang-go python3 python3-pip git wget unzip make
git clone https://github.com/SecOpsElite/Hybrid_Sub.git && cd Hybrid_Sub
python3 installers/first_run_installer.py
```

---

### ✅ Arch Linux / Manjaro
```bash
sudo pacman -Syu go python python-pip git unzip wget make
git clone https://github.com/SecOpsElite/Hybrid_Sub.git && cd Hybrid_Sub
python3 installers/first_run_installer.py
```

---

### ✅ macOS (Homebrew)
```bash
brew install go python git wget make
git clone https://github.com/SecOpsElite/Hybrid_Sub.git && cd Hybrid_Sub
python3 installers/first_run_installer.py
```

---

## 🚀 Running the Tool

### Launch Options
```bash
python hybrid_sub.py
```

You’ll see:
```
[1] Run Python Version
[2] Run Go Version
```

---

## 🧪 Use Cases

| Purpose                 | How Hybrid_Sub Helps                        |
|------------------------|---------------------------------------------|
| Bug Bounty Recon       | Finds hidden & forgotten assets             |
| Red Team Targeting     | Identifies shadow infrastructure            |
| WAF/Edge Bypass        | Detects wildcard and DNS-edge conditions    |
| Continuous Recon       | Supports automation, logging, and expansion |

---

## 🔧 Customization

- `wordlists/dns.txt`: Add your own brute-force subdomain entries
- `resolvers.txt`: Add DNS resolvers (public, trusted)
- `configs/plugin_config.json`: Toggle plugins and API keys

---

## 🔌 Plugin System

Create new plugins by dropping `.py` files into the `plugins/` folder with a `run(domain, api_key)` function. Hybrid_Sub auto-detects and runs them if enabled in `plugin_config.json`.

---

## 📂 Project Structure

```
Hybrid_Sub/
├── python_core/         # Python logic
├── go_core/             # Go-based scanner
├── plugins/             # Custom plugins
├── installers/          # Windows/Mac/Linux installer scripts
├── wordlists/           # DNS & resolver lists
├── configs/             # API keys and settings
├── hybrid_sub.py        # Launcher
├── final_subdomains.txt # Combined output
```

---

## 🛡 Legal Disclaimer

This tool is intended for authorized security testing and educational use only. Unauthorized use is prohibited.

---

## 💬 Support

Issues and PRs welcome: [github.com/SecOpsElite/Hybrid_Sub](https://github.com/SecOpsElite/Hybrid_Sub)

---

## 📌 Final Tip

Make sure:
- Python ≥ 3.7
- Go ≥ 1.20
- Git, curl, and unzip are installed

Then simply:
```bash
python hybrid_sub.py
```
And you’re ready to hunt 🎯
