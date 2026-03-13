import requests
import os
import argparse
import pyfiglet
print("")
print("")

print(pyfiglet.figlet_format(text="dominic",font="smblock"),end="")
print("domain status check")


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", required=True, help="wordlist path") 
args = parser.parse_args()


if not os.path.exists(args.domain):
    print(f"[!] '{args.domain}' not found.")
    exit()
active_urls = []
nonactive = []
with open(args.domain, "r") as domains:
    print("="*50)
    print("[INFO] Requesting domains...")
    print("="*50)
    for line in domains:
        url = line.strip()
        if not url: continue       
        if not url.startswith("http"):
            url = f"http://{url}"
        try:
         response = requests.get(url, timeout=5)
         if response.ok:
            active_urls.append(url)
         else:
            pass
        except requests.exceptions.RequestException:
           nonactive.append(url)
           


        

