"""
listener.py

Author: Sam Hilliard

Listens for connections on a specified port and
starts an interactive shell.
That's really all there is to it.
"""

import socket
import json

class Listener:

    def __init__(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))
        s.listen()
        self.connection, self.address = s.accept()

    def recieve_data(self):
        data = ''

        while True:
            data += self.connection.recv(1024).decode('utf-8')
            try:
                return json.loads(data)
            except json.decoder.JSONDecodeError:
                continue

    def send_data(self, data):
        packaged = json.dumps(data)
        return self.connection.send(packaged.encode('utf-8'))


def main():
    print('[+] Starting Listener')
    listener = Listener('127.0.0.1', 4444)
    print('[+] Connected to ' + listener.address[0])

    command = input('^_^ >> ')
    listener.send_data(command.split(' '))
    print(listener.recieve_data())

    listener.connection.close()


if __name__ == '__main__':
    main()
    