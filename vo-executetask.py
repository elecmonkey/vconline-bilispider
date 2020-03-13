# -- coding: utf-8 --
import pymongo
import config
import time
import random
import lib.biliapi

time.sleep(3)

def getStatFunction(type, num):
    biliData = lib.biliapi.BiliAPI()
    if type == 'getstat':
        biliData.Aid = num
        getStat = biliData.getVideoData()
        myClient = pymongo.MongoClient(config.DATABASE_URL)
        myDB = myClient[config.DATABASE_INDEX]
        myCol = myDB["list"]
        if getStat['error'] == 0:
            getStat.pop('error')
            getStat['time'] = time.time()
            myDB2 = myClient[config.DATABASE_DATA]
            myCol2 = myDB2['av' + str(num)]
            myCol2.insert_one(getStat)
            myCol.delete_one({'type': type, 'num': num})
        elif getStat['error'] == 1:  # 曲目不存在
            myCol.delete_one({'type': type, 'num': num})
        elif getStat['error'] == 2:
            print("VCOnline/ExecuteTask: HTTP错误")
        myClient.close()

while True:
    exeCount = 0
    myClient = pymongo.MongoClient(config.DATABASE_URL)
    myDB = myClient[config.DATABASE_INDEX]
    myCol = myDB["list"]
    if myCol.count_documents({}) > 0:
        myResults = myCol.find().sort('_id', pymongo.ASCENDING)
        for oneResults in myResults:
            getStatFunction(oneResults['type'], oneResults['num'])
            exeCount += 1
            time.sleep(random.randint(5, 30) / 100)
    myClient.close()
    if exeCount > 0:
        print("VCOnline/ExecuteTask: 执行了" + str(exeCount) + "个数据采集任务。")