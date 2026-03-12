import urllib.request
import json
from urllib.error import URLError

def ip(args):
    color_green = "\033[32m"
    color_cyan = "\033[36m"
    color_red = "\033[31m"
    color_reset = "\033[0m"
    
    try:
        req = urllib.request.Request("https://ipinfo.io/json", headers={'User-Agent': 'curl/7.68.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            print(f"\n{color_cyan}=== Public IP & Location Info ==={color_reset}")
            print(f" IP Address : {color_green}{data.get('ip', 'Unknown')}{color_reset}")
            print(f" Hostname   : {data.get('hostname', 'Unknown')}")
            print(f" City       : {data.get('city', 'Unknown')}")
            print(f" Region     : {data.get('region', 'Unknown')}")
            print(f" Country    : {data.get('country', 'Unknown')}")
            print(f" Location   : {data.get('loc', 'Unknown')}")
            print(f" ISP        : {data.get('org', 'Unknown')}")
            print()
            return 0
    except URLError as e:
        print(f"{color_red}[-] IP service connection failed: {e.reason}{color_reset}")
        return 1
    except Exception as e:
        print(f"{color_red}[-] Error:{color_reset} {e}")
        return 1

PLUGIN_COMMANDS = {
    "ip": ip
}
