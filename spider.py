# -- coding: utf-8 --
import os
import threading
import config

class NewThreading (threading.Thread):
    taskType = ''
    def __init__(self, tT):
        self.taskType = tT
        threading.Thread.__init__(self)
    def run(self):
        if self.taskType == 'finder':
            print("VCOnline: Finder模块已启动。")
            os.system(config.PYTHON_COMMAND + ' vo-finder.py')
        if self.taskType == 'createtask':
            print("VCOnline: CreateTask模块已启动。")
            os.system(config.PYTHON_COMMAND + ' vo-createtask.py')
        if self.taskType == 'executetask':
            print("VCOnline: ExecuteTask模块已启动。")
            os.system(config.PYTHON_COMMAND + ' vo-executetask.py')

thread1 = NewThreading('finder')
thread1.start()
thread2 = NewThreading('createtask')
thread2.start()
thread3 = NewThreading('executetask')
thread3.start()
