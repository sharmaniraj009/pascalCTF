import requests
import json

def send_progress(progress):
    url = "https://kontactmi.challs.pascalctf.it/adminSupport"  # Target URL
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"code": progress})
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        print("[+] Flag found:", response.text)
    else:
        print("[-] Failed to retrieve flag. Check manually.")

def extract_flag():
    collectables = ["up", "up", "down", "down", "left", "right", "left", "right", "B", "A"]
    progress = "-".join(collectables)  # Construct the expected input
    print("[*] Sending progress:", progress)
    send_progress(progress)

if __name__ == "__main__":
    extract_flag()
