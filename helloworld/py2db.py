#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  brief: transform data from GameDB(mysql) to OSS(mongodb)
"""

import os, sys, time
import MySQLdb
import simplejson
import pymongo
from pymongo import MongoClient
from py_pb_converters import pbjson
from ProtoPY import GameData_pb2
from bson.binary import Binary

if sys.getdefaultencoding != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

userid_max = 7999999
table_count = 100
logdir = "/data/qibai/pylog/"

db = MySQLdb.connect("localhost","root","","gamedb_101_0",charset='utf8')

cursor = db.cursor()
#ret = cursor.execute("select count(*) from gametable_0")
#print "000-", ret, type(ret)
#result = cursor.fetchall()
#print result, type(result), len(result), result[0][0], type(result[0])
#result = cursor.fetchone()
#print result

#mongodb
mgclient = MongoClient('mongodb://10.5.189.230:27017')
mgdb = mgclient.game101_database
collection = mgdb.game101_collection_0

ret = os.access(logdir, os.F_OK)
if ret == False:
    os.mkdir(logdir)
    print "mkdir pylog"
else:
    print "get pylog dir"

for index in range(0, 100):
    print "Begin to scan table_%d >>>>>>>>>>>>>>>>>>>>>" % index 
    cursor.execute("select count(*) from gametable_%d" % index)
    row_result = cursor.fetchall()
    if(row_result[0][0] == 0):
        continue

    rowmark = 0
    userid = 60000000
    userid_max = userid + 199999 + 200000*index
    while (rowmark < row_result[0][0]):#(userid < userid_max):
        tableid = userid % table_count
        useridtail = userid + 1000
        #sqlstr = "select * from gametable_%d where UserID between %d and %d" % (tableid, userid, useridtail)
        #sqlstr = "select * from gametable_%d where UserID >= %d and UserID < %d" % (tableid, userid, useridtail)
        #sqlstr = "select * from gametable_%d where UserID = %d " % (tableid, userid)
        sqlstr = "select * from gametable_%d limit %d, 100" % (tableid, rowmark)
        rowmark = rowmark + 100
        ret = cursor.execute(sqlstr)
    
        result = cursor.fetchall()
        jsonlist = []
        useridlist = []
        i = 0
        for data in result :
            pbdata = GameData_pb2.GameData()
            pbdata.ParseFromString(str(data[3]))
            #print(pbdata)
            #print '-----------------------------'
            row = {} #dict
            row['userId'] = data[0]
            row['upInTime'] = int(time.time())
            #Convert Protobuf to dict   #JSoN
            game_data_dict = pbjson.pb2dict(pbdata)
            row['gameData'] = game_data_dict
            row['rowdata'] = Binary(data[3], 0)
            #print data[3]

            #rowJson = simplejson.dumps(row, indent=4)
            #rowJson = simplejson.dumps(row)  
            #print(rowJson)   
            jsonlist.append(row)
            useridlist.append(data[0])
            i = i+1
            #print(jsonlist)
            #print(useridlist)
            #print(i)
            #ret = collection.update_one({"userId":data[0]}, {'$set':{"gameData":game_data_dict}}, upsert = True)
            #if(ret.matched_count == 1 or ret.upserted_id != None):
            #    print "update ret = ", ret, type(ret), ret.upserted_id, ret.modified_count
    
        #print(len(jsonlist))
        #insert to Mongodb
        if(len(jsonlist) > 0):
            try:
                result = collection.insert_many(jsonlist)
                #print(type(result))
                #print(result.inserted_ids)
            except:
                print "mongodb insert error:", useridlist
                #for json in jsonlist:
                #    print json
                #result = collection.insert_many(jsonlist)
            else:
                print "mongodb insert success from %d limit %d from table_%d" % (rowmark, len(jsonlist), index)
            
            
    
        #log
        today = logdir + time.strftime('%Y%m%d')
        fd = os.open(today, os.O_RDWR|os.O_CREAT)
        with os.fdopen(fd, "a+") as fo :
            fo.write("%s:@table_%d :: %s\n"%(str(time.time()), index, str(useridlist)))
            #此时，指针在文件末尾
            #fo.seek(os.SEEK_SET)
            #filedata = fo.read()
            #print(filedata)
    
        #print(userid)
        userid = useridtail
        #userid = userid + 1


#gamedb--MySQL
db.close()



