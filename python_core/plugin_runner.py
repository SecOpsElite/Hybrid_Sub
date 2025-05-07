
import os
import sys
import json

# Dynamically add the utils directory to sys.path
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
utils_path = os.path.join(base_path, "utils")
if utils_path not in sys.path:
    sys.path.insert(0, utils_path)

from plugin_loader import load_plugins

def run_plugins(domain, config_file="configs/plugin_config.json"):
    try:
        with open(config_file) as f:
            config = json.load(f)
    except Exception as e:
        print(f"[!] Failed to read config: {e}")
        return []

    plugins = load_plugins()
    results = []
    for name, opts in config.items():
        if opts.get("enabled", False):
            plugin = plugins.get(name)
            if plugin:
                print(f"[+] Running plugin: {name}")
                output = plugin.run(domain, opts.get("api_key"))
                results.extend(output)
            else:
                print(f"[!] Plugin not found: {name}")
    return list(set(results))
