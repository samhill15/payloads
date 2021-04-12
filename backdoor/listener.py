"""
listener.py

Author: Sam Hilliard

Listens for connections on a specified port and
starts an interactive shell.
That's really all there is to it.
"""

import socket

class Listener:

    def __init__(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))
        s.listen()
        self.connection, self.address = s.accept()

    def recieve_data(self):
        return self.connection.recv(1024)

    def send_data(self, command):
        self.connection.send(command)


def main():
    listener = Listener('127.0.0.1', 4444)

    command = input('^_^ >> ').encode('utf-8')
    listener.send_data(command)
    print(listener.recieve_data())

    listener.connection.close()


if __name__ == '__main__':
    main()
    