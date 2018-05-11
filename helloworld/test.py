#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from py_pb_converters import pbjson
from ProtoPY import GameData_pb2

print "for test................."

pbdata = GameData_pb2.GameData()
print pbdata

game_data_dict = pbjson.pb2dict(pbdata)
print game_data_dict

print "test end"

s= '\n\x06\x08\xb3\xef\xc7\xd6\x05'
s1 = s.decode(encoding='utf-8', errors='ignore')
print s1
