# coding: utf-8

'Send an email, the content is you need'

import smtplib, os
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  

class SendEmail(object):

    def __init__(self, from_addr, password, to_addr, smtp_server, subject, attachs):
        self.from_addr = from_addr
        self.password = password
        self.to_addr = to_addr
        self.smtp_server = smtp_server
        self.subject = subject
        self.attachs = attachs

    def send(self):
        if len(self.attachs) != 0:
            msg = MIMEMultipart()
            msg['From'] = self.from_addr
            msg['To'] = self.to_addr
            msg['Subject'] = self.subject
            for attach in self.attachs:
                msg.attach(MIMEText(os.path.split(attach)[1] + " ", 'plain', 'utf-8'))
                att = MIMEText(open(attach, 'rb').read(), 'base64', 'utf-8')
                att["Content-Type"] = 'application/octet-stream'
                att["Content-Disposition"] = 'attachment; filename=' + os.path.split(attach)[1]
                msg.attach(att)
            try:
                print("Sending an email...")
                server = smtplib.SMTP(self.smtp_server)
                server.login(self.from_addr, self.password)
                server.sendmail(self.from_addr, [self.to_addr], msg.as_string())
                server.quit()
                print("Sending Success")
            except:
                print("Fail")
        else:
            print("TODO send text email")