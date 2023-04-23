#!/usr/bin/env python

import requests
import argparse

def get_args():
    parser = argparse.ArgumentParser()    
    parser.add_argument("-u", "--url", dest="url", help="Target website URL.")
    parser.add_argument("-w", "--wordlist", dest="wordlist", default="subdomains-wordlist.txt", help="Optional wordlist.")
    args = parser.parse_args()
    return args

def request(url):
    try:
        return requests.get("http://" + url)
    except Exception:
        pass

args = get_args()
target = args.url
wordlist = args.wordlist
    
with open(wordlist, "r") as f:
    for line in f:
        domain = line.strip()
        test_url = f"{domain}.{target}"
        response = request(url=test_url)
        if response:
            print(f"\u001b[38;5;231m[*] Discovered subdomain ==> \u001b[38;5;47m{test_url}")

print("\n\u001b[38;5;226mDone.")