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

Domain crawler:
```sh
# Full search (default wordlist):
$ python dsearch.py -u <target_url>

# With custom wordlist:
$ python dsearch.py -u <target_url> -w <wordlist.txt>
```

## Example