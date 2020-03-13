# -- coding: utf-8 --
from gevent import monkey
monkey.patch_all()

from flask import Flask
from gevent import pywsgi
from flask_restful import reqparse, abort, Api, Resource
import pymongo
import config


webapi = Flask(__name__)
api = Api(webapi)

parser = reqparse.RequestParser()
parser.add_argument('aid', location=['json', 'args'], type = dict)

class video(Resource):
    def get(self, video_id):
        myClient = pymongo.MongoClient(config.DATABASE_URL)
        myDB = myClient[config.DATABASE_INDEX]
        myCol = myDB["songs"]
        myQuery = {"aid": int(video_id)}
        myDoc = myCol.find(myQuery)
        myDoc_r = {}
        for myDoc_s in myDoc:
            myDoc_r = myDoc_s
        if myDoc_r == {}:
            abort(404, error="1")
        myDoc_r.pop('_id')
        return myDoc_r

    def delete(self, video_id):
        abort(503, error="1")

    def put(self, video_id):
        pass

# 监听Url地址
api.add_resource(video, '/videos/info/<video_id>')

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 3200), webapi)
    print('RESTfulAPI server start')
    server.serve_forever()
