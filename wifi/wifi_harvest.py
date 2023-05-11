#!/usr/bin/env python
import subprocess as sp
import re
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--file", dest="output_file", help="Text file name to save output")
    args = parser.parse_args()
    if not args.output_file:
        parser.error("[!] Specify output file name")
    return args

args = get_args()
output_file = args.output_file

def save(file):
    with open(f'{output_file}.txt', 'w') as f:
        for key, value in file.items():
            f.write(f"{key}: {value}\n")
    print("\u001b[32mFile saved successfully 💾.\u001b[0m")
    
command = "netsh wlan show profiles"
networks = sp.check_output(command, shell=True)
network_names_list = re.findall(r"(?:Profile\s*:\s)(.*)", networks.decode())
wifi_harvester = {}

for network in network_names_list:
    get_wifi = f'netsh wlan show profile "{network}" key=clear'
    bin_password = sp.check_output(get_wifi, shell=True)
    password = re.search(r"Key Content\s*:\s*(.*)", bin_password.decode()).group(1)

    wifi_harvester[network.replace("\r", "")] = password.replace("\r", "")

save(wifi_harvester)