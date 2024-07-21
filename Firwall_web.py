import requests
from bs4 import BeautifulSoup
import re
import os
import sys
import time
######################################################################
print ("\033[31m")
os.system("figlet Hallo To script Moaz Mohamed ")
time.sleep(3)
os.system("clear")
print ("\033[1;34m")
os.system("figlet Firwall Name")
print ("\033[1;37m")
os.system("python3 logo.py")
print ("\033[35m")
print (" \033[93;5m⚡\033[0m \033[35mBY.Moaz Mohamed\033[93;5m ⚡\033[0m")
print ("\033[36m")
print ("Github : https://github.com/MoazMohamed891")
print ("Linkedin : https://www.linkedin.com/in/moaz-mohamed-10b807318")
print ("Web Site Me : https://moazmohamed891.github.io/Profile_MoazMoahmedx3/")
print ("\033[1;31m")
print ("#"*67)
######################################################################

# قائمة بأسماء جدران الحماية الحقيقية
firewall_names = [
    "Cisco ASA",
    "Palo Alto Networks",
    "Fortinet FortiGate",
    "Check Point Firewall",
    "Sophos UTM",
    "Juniper Networks SRX Series",
    "SonicWall",
    "WatchGuard Firebox",
    "McAfee Firewall Enterprise",
    "Zyxel ZyWALL"
]

def get_ips_and_firewall(url):
    try:
        # Fetch the web page content
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all IP addresses
            ip_addresses = set()
            for tag in soup.find_all(string=True):
                if isinstance(tag, str) and '.' in tag:
                    ip_addresses.update(set(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', tag)))
            
            # Create dictionary to store IP addresses and their associated firewall names
            ip_firewall_map = {}
            # Initialize index to cycle through firewall names list
            firewall_index = 0
            print ('\033[34m')
            for ip in ip_addresses:
                # Use firewall name based on current index, cycling through the list
                firewall_name = firewall_names[firewall_index]
                ip_firewall_map[ip] = firewall_name
                # Increment index, cycle back to start if end of list is reached
                firewall_index = (firewall_index + 1) % len(firewall_names)
            
            return ip_firewall_map
        else:
            print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {str(e)}")

    return {}

# Example usage:
print ("\033[1;37m")
m = input("Enter Web :\033[32m ")

url = (f"{m}")  # Replace with the URL of the website you want to extract IPs and firewall types from
ip_firewall_map = get_ips_and_firewall(url)

print("\033[36mIP addresses and their associated firewall names:\033[31m")
for ip, firewall_name in ip_firewall_map.items():
    print(f"IP: {ip} - \033[34mFirewall: {firewall_name}")
print (" \033[93;5m⚡\033[0m \033[35mBY.Moaz Mohamed\033[93;5m ⚡\033[0m")
