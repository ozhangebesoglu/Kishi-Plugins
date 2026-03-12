import urllib.request
import urllib.parse
from urllib.error import URLError

def qr(args):
    color_red = "\033[31m"
    color_reset = "\033[0m"
    
    if len(args) < 2:
        print("Usage: qr <text-or-url>")
        return 1
        
    text = args[1]
    url = f"https://qrenco.de/{urllib.parse.quote(text)}"
    
    print(f"[*] Generating QR Code for '{text}'...")
    try:
        # qrenco.de automatically serves ASCII QR codes to terminal user agents like curl
        req = urllib.request.Request(url, headers={'User-Agent': 'curl/7.68.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read().decode('utf-8')
            print()
            print(data)
            print()
            return 0
    except URLError as e:
        print(f"{color_red}[-] QR service connection failed: {e.reason}{color_reset}")
        return 1
    except Exception as e:
        print(f"{color_red}[-] Error:{color_reset} {e}")
        return 1

PLUGIN_COMMANDS = {
    "qr": qr
}
