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
    print(f"[!] '{args.domain}' no fue encontrado.")
    exit()

with open(args.domain, "r") as domains:
    print("="*50)
    print("[:] Requesting domains...")
    print("="*50)
    for line in domains:
        url = line.strip()
        if not url: continue 
       
        if not url.startswith("http"):
            url = f"http://{url}"
        
        try:
            response = requests.get(url, timeout=5)
            print(f"\n{url}")
            print(f"STATUS CODE : {response.status_code}")
           

            
            try:
                print("CONTENT (JSON):")
                print(response.json())
            except requests.exceptions.JSONDecodeError:
                print("CONTENT (TEXT):")
                print(response.text[:200]) 
                
        except requests.exceptions.RequestException as e:
            print(f"\n[!] Error conectando a {url}: {e}")
        
      

