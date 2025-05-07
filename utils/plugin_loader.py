
import os
import importlib.util

PLUGIN_DIR = os.path.join(os.path.dirname(__file__), "..", "plugins")

def load_plugins():
    plugins = {}
    if not os.path.exists(PLUGIN_DIR):
        print("[!] Plugins directory not found.")
        return plugins

    for file in os.listdir(PLUGIN_DIR):
        if file.endswith(".py") and not file.startswith("_"):
            plugin_name = file[:-3]
            plugin_path = os.path.join(PLUGIN_DIR, file)
            try:
                spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                plugins[plugin_name] = module
            except Exception as e:
                print(f"[!] Failed to load plugin {plugin_name}: {e}")
    return plugins
