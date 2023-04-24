# Website Crawlers

## Description
Crawl website domains and paths with custom wordlist or default one (full search).

<ul>
    <li>Domain crawler - <b>dsearch.py</b></li>
    <li>Path crawler - <b>rsearch.py</b></li>
</ul>

### Requirements
Python v3

## Run

<i>note: speed will be depanding on your internet speed and target website.</i>

Subdomain crawler:
```sh
# Advanced search (default wordlist: ~65K words):
$ python dsearch.py -u <target_url> --full

# Normal search (default wordlist: ~10K words)
$ python dsearch.py -u <target_url>

# With custom wordlist:
$ python dsearch.py -u <target_url> -w <wordlist.txt>
```

## Example