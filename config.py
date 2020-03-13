# -- coding: utf-8 --

# Python运行命令
PYTHON_COMMAND = 'python'

# MongoDB数据库地址
DATABASE_URL = 'mongodb://localhost:27017/'
# 保存视频信息的数据库
DATABASE_INDEX = 'vconline'
# 保存爬虫数据的数据库
DATABASE_DATA = 'vconline_data'
# DATABASE_USERNAME = 'admin'
# DATABASE_PASSWORD = 'admin'

#允许添加的视频TAG
TAG = ['VOCALOID中文曲', '中文VOCALOID', 'VOCALOID', 'UTAT',
       '中文UTAU', 'UTAU中文曲', 'SynthV', 'Synthesizer V',
       'Synth V', 'SynthesizerV', 'Deepvocal', 'Deepvocal中文曲',
       '中文Deepvocal']

# 以下均为未实现功能
"""
FILE_TYPE = 'local'
 # bilibili：保留B站原始URL local：保存在本地 oss：保存到阿里云对象储存 cos：保存到腾讯云对象储存
OSS_AK = ''
OSS_SK = ''
OSS_BUCKET = ''
OSS_DOMAIN = ''
"""