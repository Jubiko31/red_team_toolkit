#!/usr/bin/env python
import scapy.all as scapy
from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Target interface to monitor")
    args = parser.parse_args()
    
    return args

def get_mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast / arp_req
    ans = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    
    return ans[0][1].hwsrc

def sniff(interface):
    scapy.sniff(iface=interface, stop=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        try:
            mac = get_mac(packet[scapy.ARP].psrc)
            response_mac = packet[scapy.ARP].hwsrc
            if mac != response_mac:
                print("\u001b[38;5;202m[!!] Detected ARP spoofing...\nSource: {mac}")
        except IndexError:
            pass
       
args = get_args()
sniff(args.interface)