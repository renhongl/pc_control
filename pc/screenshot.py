import pyscreenshot as ImageGrab
from datetime import datetime
import os, sendEmail
from constant import Constant as C

class ScreenShot(object):
    def __init__(self):
        self.dir = os.path.abspath(C.SCREEN_DIR)

    def __createDir(self):
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        else:
            if os.path.exists(os.path.join(self.dir, C.SCREEN_IMG)):
                os.remove(os.path.join(self.dir, C.SCREEN_IMG))

    def grab(self):
        self.__createDir()
        now = datetime.now()
        nowTime = now.timestamp()
        name = str(nowTime).split(".")[0]
        print(self.dir)
        im = ImageGrab.grab_to_file(os.path.join(self.dir, C.SCREEN_IMG))
        print(im)
        print("Taking Successfully")
        from_addr = C.EMAIL_126
        password = C.PWD
        to_addr = C.EMAIL_QQ
        smtp_server = C.SMTP_126_SERVER
        subject = C.TEST_SUBJECT
        attachs = [os.path.join(self.dir, C.SCREEN_IMG)]
        se = sendEmail.SendEmail(from_addr, password, to_addr, smtp_server, subject, attachs)
        se.send()
        

