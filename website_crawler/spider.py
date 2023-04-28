#!/usr/bin/env python

import requests
import argparse
import sys
import re
from urllib.parse import urlparse
from urllib.parse import urljoin
from datetime import datetime

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", dest="url", help="Target website URL. Example: http://example.com", required=True)
    args = parser.parse_args()
    return args

def req(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))
    
def spider(url):
    links = req(url)
    for link in links:
        link = urljoin(url, link)
        if "#" in link:
            link = link.split("#")[0]         
        if target in link and link not in target_links:
            target_links.append(link)
            print(f"\u001b[38;5;47m{link}")
            spider(link)

args = get_args()
target = args.url
target_links = []

print(f"\u001b[38;5;226mTarget: \u001b[38;5;33mhttps://{target}")
print(f'\n\u001b[38;5;226m[{datetime.now().strftime("%H:%M:%S")}] 🕷️ Started Spider')

if __name__ == '__main__':
    spider(target)

print(f'\n\u001b[38;5;226m[{datetime.now().strftime("%H:%M:%S")}] Done.')