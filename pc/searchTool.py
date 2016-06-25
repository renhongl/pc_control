# coding: utf-8

'Find something from laptop'

import os, sendEmail, threading
from constant import Constant as C

class SearchTool(object):
    
    def __parseFile(self, file):
        if not self.searchName and os.path.splitext(file)[1].lower() == self.searchFile.lower():

            with open(os.path.join(self.dataPath, C.URL_PATH), "a") as output:
                output.write("File %d : %s\n" % (self.count, file))

            print("File %d : %s" % (self.count, file))
            self.count += 1

        elif self.searchName and os.path.split(file)[1].lower().split(".")[0] == self.searchFile.lower():
            with open(os.path.join(self.dataPath, C.URL_PATH), "a") as output:
                output.write("File %d : %s\n" % (self.count, file))

            print("File %d : %s" % (self.count, file))
            self.count += 1
        

    def __init__(self, searchPath, searchFile, searchName):
        self.searchPath = searchPath
        self.searchFile = searchFile
        self.count = 1
        self.searchLenth = 20
        self.dataPath = os.getcwd()
        self.searchName = searchName
        if os.path.exists(os.path.join(self.dataPath, C.URL_PATH)):
            os.remove(os.path.join(self.dataPath, C.URL_PATH))
        
    def parsePath(self, path):
        if os.path.isdir(path):
            try:
                os.chdir(path)
                dirGroup = [os.path.abspath(dir) for dir in os.listdir(path) if os.path.isdir(dir)]
                fileGroup = [os.path.abspath(file) for file in os.listdir(path) if os.path.isfile(file)]
                
                if len(fileGroup) != 0:
                    for oneFile in fileGroup:
                        self.__parseFile(oneFile)
                if len(dirGroup) != 0:
                    for oneDir in dirGroup:
                        self.parsePath(oneDir)
            except:
                print("%s can not open" % path)
        else:
            print("%s not a dir" % path)
        




