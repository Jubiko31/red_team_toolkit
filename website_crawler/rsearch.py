#!/usr/bin/env python

import argparse

def get_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("-u", "--url", dest="url", help="Target website URL.", required=True)
    group.add_argument("--full", help="Do a advance scan.", action='store_true')
    group.add_argument("-w", "--wordlist", dest="wordlist", default="wordlists/path_common.txt", help="Optional wordlist.")
    args = parser.parse_args()
    return args
