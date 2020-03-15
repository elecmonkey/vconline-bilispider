# -- coding: utf-8 --
from flask import Flask, request, make_response, Response
from gevent import monkey
import pymongo
import config
import time
import json

monkey.patch_all()
app = Flask("vconline-bilispider")

@app.route('/songs/<aid>', methods=['GET'])
def songs(aid):
    myClient = pymongo.MongoClient(config.DATABASE_URL)
    myDB = myClient[config.DATABASE_INDEX]
    myCol = myDB["songs"]
    myQuery = {"aid": int(aid)}
    myDoc = myCol.find(myQuery)
    myDoc_r = {}
    for myDoc_s in myDoc:
        myDoc_r = myDoc_s
    if myDoc_r == {}:
        return { }, 404
    myDoc_r.pop('_id')
    res = Response(json.dumps(myDoc_r))
    res.headers.add("Access-Control-Allow-Origin", "*")
    # res.set_cookie('a','b',time.time()+360)
    return res

@app.route('/songs/<aid>/data', methods=['GET'])
def songs_data(aid):
    myTime = int(request.args.get('time'))
    myClient = pymongo.MongoClient(config.DATABASE_URL)
    myDB = myClient[config.DATABASE_DATA]
    myCol = myDB["av" + str(aid)]
    myDoc = myCol.find({}) .sort("time", -1)
    myDoc_r = ''
    myTimeD = 0
    i = 0
    for myDoc_one in myDoc:
        if i == 0:
            myTimeD = abs(myTime - myDoc_one['time'])
            myDoc_r = myDoc_one
        i += 1
        myTimeDt = abs(myTime - myDoc_one['time'])
        if myTimeDt > myTimeD:
            break
        myDoc_r = myDoc_one
        myTimeD = myTimeDt

    myDoc_r.pop("_id")
    res = Response(json.dumps(myDoc_r))
    res.headers.add("Access-Control-Allow-Origin", "*")
    # res.set_cookie('a','b',time.time()+360)
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3200, debug=True)

