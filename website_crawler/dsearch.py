#!/usr/bin/env python

import requests
import argparse
import sys
from datetime import datetime

def get_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("-u", "--url", dest="url", help="Target website URL.", required=True)
    group.add_argument("--full", help="Do a advance scan with ~65K words.", action='store_true')
    group.add_argument("-w", "--wordlist", dest="wordlist", default="wordlists/domain_common.txt", help="Optional wordlist.")
    args = parser.parse_args()
    return args

def request(url):
    try:
        return requests.get("http://" + url, timeout=3)
    except Exception:
        pass
    
def crawl(filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            print(f'\u001b[38;5;14m### Progress {i+1}/{size}', end="\r")
            try:
                domain = line.strip()
                test_url = f"{domain}.{target}"
                response = request(url=test_url)
                try: 
                    if response or isinstance(response.status_code, int):
                        print(f"\u001b[38;5;231m[*] Discovered subdomain ==> \u001b[38;5;13m[{response.status_code}] \u001b[38;5;47m{test_url}")
                except Exception:
                    pass
            except KeyboardInterrupt: 
                print("\u001b[38;5;255mCTLR+C detected. Cancel job?")
                c = input("[q]uit/[c]ontinue: ")
                if c.lower() == "c":
                    continue
                else:
                    print("\n\u001b[41;1m\u001b[38;5;255mcanceled.\u001b[0m")
                    sys.exit() 

args = get_args()
target = args.url
if args.full:
    wordlist = "wordlists/domain_full.txt"
else:
    wordlist = args.wordlist
with open(wordlist) as f:
    size = sum(1 for _ in f)

print(f"\u001b[38;5;226mTarget: \u001b[38;5;33mhttps://{target}   \u001b[38;5;226m Words: \u001b[38;5;93m{size}", end="\r")
print(f'\n\u001b[38;5;226m[{datetime.now().strftime("%H:%M:%S")}] Started:')

if __name__ == '__main__':
    crawl(wordlist)

print(f'\n\u001b[38;5;226m[{datetime.now().strftime("%H:%M:%S")}] Done.')