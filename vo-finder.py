# -- coding: utf-8 --
import lib.biliapi
import config
import pymongo
import random
import time
# 从数据库中的source集合读取数据源信息，并进行抓取。
# 每个文档有三个字段。
# type为数据源类型，可以为folder（收藏夹）或up（UP主）.
# num为数据源信息，可以为收藏夹的fid或UP主的uid。

while True:
    addCount = 0
    startTime = time.time()
    myClient = pymongo.MongoClient(config.DATABASE_URL)
    myDB = myClient[config.DATABASE_INDEX]
    myCol = myDB["source"]
    myColSongs = myDB["songs"]
    biliData = lib.biliapi.BiliAPI()
    for oneCol in myCol.find({}, no_cursor_timeout = True):
        if oneCol['type'] == 'folder':
            biliData.Fid = oneCol['num']
            folderDic = biliData.getFolder()
        if oneCol['type'] == 'up':
            biliData.Uid = oneCol['num']
            folderDic = biliData.getUpperVideo()
        for oneValue in range(1, len(folderDic)):
            if myColSongs.count_documents({'aid': folderDic[oneValue]}) == 0:
                biliData.Aid = folderDic[oneValue]
                isTagOk = False
                videoTag = biliData.getVideoTag()
                if videoTag['error'] == 0:
                    videoTag.pop("error")
                    for videoTagNum in videoTag:
                        for allowableTag in config.TAG:
                            if videoTag[videoTagNum].lower() == allowableTag.lower():
                                isTagOk = True
                    if isTagOk:
                        videoInfo = biliData.getVideoInfo()
                        if videoInfo['error'] == 0:
                            videoInfo.pop('error')
                            videoInfo['aid'] = folderDic[oneValue]
                            videoInfo['group'] = 2
                            myColSongs.insert_one(videoInfo)
                            addCount += 1
                            print("VCOnline/Finder: 添加了视频：" + videoInfo['title'] + "，这是第" + str(addCount) + "首。")
                            time.sleep(random.randint(5, 30) / 100)
    print("VCOnline/Finder: 完成一次新曲目采集，共耗时：" + str(time.time() - startTime) + "秒钟。")
    time.sleep(600)
