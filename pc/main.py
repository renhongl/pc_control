# coding: utf-8

'Start file of this project'

import searchTool, readEmail, time, sendEmail, screenshot
import smtplib, os
from threading import Timer

class Main(object):

    def __init__(self, timer_interval, email, pwd, pop3_server, searchPath):
        self.timer_interval = timer_interval
        self.email = email
        self.pwd = pwd
        self.pop3_server = pop3_server
        self.searchPath = searchPath

    def __testSearchTool(self):
        searchPath = "d:\\"
        searchFile = ".mp4"
        searchName = False
        if len(searchFile.split(".")) == 1:
            searchName = True
        st = searchTool.SearchTool(searchPath, searchFile, searchName)
        st.parsePath(st.searchPath)

    def __testReadEmail(self):
        email = "liang_renhong@163.com"
        pwd = "111621116"
        pop3_server = "pop.163.com"
        searchPath = "d:\\"
        re = readEmail.ReadEmail(email, pwd, pop3_server, searchPath)
        content = re.downloadEmail()
        msg = re.parseContent(content)
        re.print_info(msg)

    def __testSendEmail(self):
        from_addr = "liang_renhong@163.com"
        password = "111621116"
        to_addr = "1075220132@qq.com"
        smtp_server = "smtp.163.com"
        subject = "test send email"
        attachs = ["C:/Users/renhongl/Desktop/PC/screenshot/1466393638.png", "C:/Users/renhongl/Desktop/PC/screenshot/1466393650.png"]
        se = sendEmail.SendEmail(from_addr, password, to_addr, smtp_server, subject, attachs)
        se.send()

    def __testScreenshot(self):
        if __name__ == "__main__":
            ss = screenshot.ScreenShot(5)
            ss.grab()

    def run(self):
        #**********Run code***************************
        re = readEmail.ReadEmail(email, pwd, pop3_server, searchPath)
        content = re.downloadEmail()
        msg = re.parseContent(content)
        re.print_info(msg)
        t = Timer(main.timer_interval, self.run)
        t.start()
        #**********************************************

        #************Test case*************************
        # self.__testSearchTool()
        # self.__testSendEmail()
        #self.__testReadEmail()
        #sself.__testScreenshot()
        #**********************************************

timer_interval = 60 * 60
email = "liang_renhong@163.com"
pwd = "111621116"
pop3_server = "pop.163.com"
searchPath = "e:\\"

main = Main(timer_interval, email, pwd, pop3_server, searchPath)
main.run()