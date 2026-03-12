import urllib.request
import urllib.parse
from urllib.error import URLError

def weather(args):
    # Kishi Shell colors
    color_cyan = "\033[36m"
    color_red = "\033[31m"
    color_reset = "\033[0m"
    
    # If no argument is provided, wttr.in auto-detects based on IP
    location = args[1] if len(args) > 1 else ""
    # format=3 gives a compact 1-line format (e.g. City: ⛅️ +15°C)
    url = f"https://wttr.in/{urllib.parse.quote(location)}?format=3"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'curl/7.68.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = response.read().decode('utf-8').strip()
            if not data or "Unknown location" in data:
                print(f"{color_red}[-] Location not found or service unavailable.{color_reset}")
                return 1
            print(f"{color_cyan}{data}{color_reset}")
            return 0
    except URLError as e:
        print(f"{color_red}[-] Weather service connection failed: {e.reason}{color_reset}")
        return 1
    except Exception as e:
        print(f"{color_red}[-] Error:{color_reset} {e}")
        return 1

PLUGIN_COMMANDS = {
    "weather": weather
}
