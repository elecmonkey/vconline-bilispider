# -- coding: utf-8 --

import json
iniFile = open('config.json', encoding = "utf-8")
iniData = iniFile.read()
iniFile.close()
iniJson = json.loads(iniData)
print(iniJson)
# Python运行命令
PYTHON_COMMAND = iniJson['python_command']

# MongoDB数据库地址
DATABASE_URL = iniJson['database']['url']
# 保存视频信息的数据库
DATABASE_INDEX = iniJson['database']['index']
# 保存爬虫数据的数据库
DATABASE_DATA = iniJson['database']['data']
# DATABASE_USERNAME = 'admin'
# DATABASE_PASSWORD = 'admin'

#允许添加的视频TAG
TAG = iniJson['tag']

# 以下均为未实现功能
"""
FILE_TYPE = 'local'
 # bilibili：保留B站原始URL local：保存在本地 oss：保存到阿里云对象储存 cos：保存到腾讯云对象储存
OSS_AK = ''
OSS_SK = ''
OSS_BUCKET = ''
OSS_DOMAIN = ''
"""