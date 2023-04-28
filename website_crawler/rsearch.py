#!/usr/bin/env python

import requests
import argparse
import sys
from datetime import datetime

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", dest="url", help="Target website URL.", required=True)
    parser.add_argument("-w", "--wordlist", dest="wordlist", default="wordlists/path_common.txt", help="Optional wordlist.")
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
                path = line.strip()
                target_url = f"{target}/{path}"
                response = request(url=target_url)
                try: 
                    if not response.status_code == 404:
                        print(f"\u001b[38;5;231m[*] Discovered path ==> \u001b[38;5;13m[{response.status_code}] \u001b[38;5;47m{target_url}")
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
wordlist = args.wordlist
with open(wordlist) as f:
    size = sum(1 for _ in f)

print(f"\u001b[38;5;226mTarget: \u001b[38;5;33mhttps://{target}   \u001b[38;5;226m Words: \u001b[38;5;93m{size}", end="\r")
print(f'\n\u001b[38;5;226m[{datetime.now().strftime("%H:%M:%S")}] Started:')

if __name__ == '__main__':
    crawl(wordlist)

print(f'\n\u001b[38;5;226m[{datetime.now().strftime("%H:%M:%S")}] Done.')