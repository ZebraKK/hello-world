#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  brief: update gamedate for OSS mongodb at regular time
"""

import os, time, threading
import datetime

import MySQLdb
import pymongo
from pymongo import MongoClient
from py_pb_converters import pbjson
from ProtoPY import GameData_pb2
from bson.binary import Binary

logdir = "/data/qibai/pylog/"

def loopFun():
    i = 0
    hour_mark = 25;#小时取值范围 0~23
    while (i < 10):
        hour_cur = time.localtime(time.time())
        print "run a loop at:", time.time(), i
        i = i+1
        #time.sleep(60)
        
        if(hour_cur == hour_mark):
            time.sleep(600)
        else:
            hour_mark = hour_cur
            #1.连接gamedb
            db = MySQLdb.connect("localhost","qibai","qibai","gamedb_0",charset='utf8')
            cursor = db.cursor()
            #  mongodb
            mgclient = MongoClient('mongodb://10.5.189.230:27017')
            mgdb = mgclient.test_database
            collection = mgdb.test_collection

            #2.循环拉取1000个, 更新mongodb
            cursor.execute("select count(*) from gametable_0")
            row_result = cursor.fetchall()
            print "now row cnt = ", row_result[0][0]

            while(row_result[0][0] > 0):#gametable size > 0
                sqlstr = "select * from gametable_0 limit 1000"
                ret = cursor.execute(sqlstr)
                result = cursor.fetchall()
                jsonlist = []
                useridlist = []
                deleteidlist = []

                #generate data of jason style
                for data in result:
                    pbdata = GameData_pb2.GameData()
                    pbdata.ParseFromString(str(data[3]))
                    row = {}
                    row['userId'] = data[0]
                    row['upInTime'] = int(time.time())
                    game_data_dict = pbjson.pb2dict(pbdata)
                    row['gameData'] = game_data_dict
                    row['rowdata'] = Binary(data[3], 0)
                    jsonlist.append(row)
                    useridlist.append(data[0])

                    #update mogodb
                    try:
                        ret = collection.update_one({"userId":data[0]}, {'$set':{"gameData":game_data_dict}}, upsert = True)
                    except:
                        print "update failed", data[0]
                    else:
                    #3.写成功清除  delete gamedb
                        if(ret.matched_count == 1 or ret.upserted_id != None):
                            cursor.execute("delete from gametable_0 where UserID = %d" % data[0])
                            deleteidlist.append(data[0])

                #update mogodb 批量???
                #if(len(jsonlist) > 0):
                #    result = collection.insert_many(jsonlist)
                #log
                updatelog = logdir + time.strftime('%Y%m%d') + "_update"
                fd = os.open(updatelog, os.O_RDWR|os.O_CREAT)
                with os.fdopen(fd, "a+") as fo:
                    fo.write("%s:%s\n" % (str(time.time()), str(useridlist)))

                #log
                deletelog = logdir + time.strftime('%Y%m%d') + "_delete"
                fd = os.open(deletelog, os.O_RDWR|os.O_CREAT)
                with os.fdopen(fd, "a+") as fo:
                    fo.write("%s:%s\n" % (str(time.time()), str(deleteidlist)))

                cursor.execute("select count(*) from gametable_0")
                row_result = cursor.fetchall()
                print "now row cnt = ", row_result[0][0]

            #4.close GameDB连接
            db.close()

    print "loopFun end"


if __name__ == '__main__':
    print "hello world"

    task = threading.Thread(target=loopFun, name='MyThread')
    task.start()

    task.join()

    print("thread %s ended" % threading.current_thread().name) 