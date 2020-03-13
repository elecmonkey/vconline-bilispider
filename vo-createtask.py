# -- coding: utf-8 --
import pymongo
import config
import time
import threading
import os


class NewThreading (threading.Thread):
    nowCount = 0
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            fileCount = 0
            if os.path.isfile("createtask.count"):
                countFile = open('createtask.count', 'r+')
                self.nowCount = int(countFile.read())
                fileCount = self.nowCount
            else:
                countFile = open('createtask.count', 'w')
            self.nowCount += 1
            fileCount += 1
            if self.nowCount == 1440:
                fileCount = 0
            countFile.seek(0)  # 文件指针
            countFile.write(str(fileCount))
            countFile.close()

            myClient = pymongo.MongoClient(config.DATABASE_URL)
            myDB = myClient[config.DATABASE_INDEX]
            myCol = myDB["songs"]
            addCount = 0
            for oneCol in myCol.find():
                if oneCol['group'] == 0:
                    pass
                elif oneCol['group'] == 1:
                    if self.nowCount % 5 == 2:
                        taskDic = {'type': 'getstat', 'num': oneCol['aid']}
                        myCol2 = myDB["list"]
                        myCol2.insert_one(taskDic)
                        addCount += 1
                elif oneCol['group'] == 2:
                    if self.nowCount % 15 == 2:
                        taskDic = {'type': 'getstat', 'num': oneCol['aid']}
                        myCol2 = myDB["list"]
                        myCol2.insert_one(taskDic)
                        addCount += 1
                elif oneCol['group'] == 3:
                    if self.nowCount % 30 == 2:
                        taskDic = {'type': 'getstat', 'num': oneCol['aid']}
                        myCol2 = myDB["list"]
                        myCol2.insert_one(taskDic)
                        addCount += 1
                elif oneCol['group'] == 4:
                    if self.nowCount % 60 == 2:
                        taskDic = {'type': 'getstat', 'num': oneCol['aid']}
                        myCol2 = myDB["list"]
                        myCol2.insert_one(taskDic)
                        addCount += 1
                elif oneCol['group'] == 5:
                    if self.nowCount % 120 == 2:
                        taskDic = {'type': 'getstat', 'num': oneCol['aid']}
                        myCol2 = myDB["list"]
                        myCol2.insert_one(taskDic)
                        addCount += 1
                elif oneCol['group'] == 6:
                    if self.nowCount % 720 == 2:
                        taskDic = {'type': 'getstat', 'num': oneCol['aid']}
                        myCol2 = myDB["list"]
                        myCol2.insert_one(taskDic)
                        addCount += 1
                elif oneCol['group'] == 7:
                    if self.nowCount == 2:
                        taskDic = {'type': 'getstat', 'num': oneCol['aid']}
                        myCol2 = myDB["list"]
                        myCol2.insert_one(taskDic)
                        addCount += 1
                elif oneCol['group'] == 8:
                    taskDic = {'type': 'getstat', 'num': oneCol['aid']}
                    myCol2 = myDB["list"]
                    myCol2.insert_one(taskDic)
                    addCount += 1
            myClient.close()
            if addCount > 0:
                print("VCOnline/CreateTask: 创建了" + str(addCount) + "个数据采集任务。")
            time.sleep(60)

thread = NewThreading()
thread.start()