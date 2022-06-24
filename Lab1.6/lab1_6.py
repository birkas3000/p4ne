import re
import glob

from ipaddress import IPv4Interface as IPv4

def convert(ip_data):

    ip = re.match("^ ip address ([0-9.]+) ([0-9.]+)$", ip_data)
    if ip:
        return {"ip":IPv4(str(ip.group(1)) + "/" + str(ip.group(2)))}
    
    return ("NoneType",)

ip_addresses = []

for current_file in glob.glob(r'..\config_files\*.txt'):
    with open(current_file) as f:
        for ip_line in f:
            c = convert(ip_line)
            if 'ip' in c:
                ip_addresses.append(c)

for i in range(len(ip_addresses)):
    print(ip_addresses[i])
