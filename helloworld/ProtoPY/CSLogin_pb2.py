# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CSLogin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import UserData_pb2
import GameData_pb2
import Response_pb2
import Match_pb2
import CommonDef_pb2
import CSCommon_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='CSLogin.proto',
  package='pb',
  serialized_pb=_b('\n\rCSLogin.proto\x12\x02pb\x1a\x0eUserData.proto\x1a\x0eGameData.proto\x1a\x0eResponse.proto\x1a\x0bMatch.proto\x1a\x0f\x43ommonDef.proto\x1a\x0e\x43SCommon.proto\"\xa1\x03\n\x0cLoginGameReq\x12$\n\x0b\x43hannelData\x18\x01 \x01(\x0b\x32\x0f.pb.ChannelData\x12\x1e\n\x08\x42\x61seData\x18\x02 \x01(\x0b\x32\x0c.pb.BaseData\x12\x11\n\tSceneType\x18\x03 \x01(\r\x12\x0f\n\x07Version\x18\x04 \x01(\r\x12\x0e\n\x06\x43ookie\x18\x05 \x01(\t\x12\x1e\n\x08Platform\x18\x07 \x01(\x0e\x32\x0c.pb.Platform\x12\x1a\n\x06\x44\x65vice\x18\x08 \x01(\x0e\x32\n.pb.Device\x12\x1c\n\x07\x41ppType\x18\t \x01(\x0e\x32\x0b.pb.AppType\x12\x0e\n\x06\x41\x64\x46rom\x18\n \x01(\r\x12\x19\n\x11\x46romAnotherServer\x18\x0b \x01(\x08\x12\x38\n\x15\x41\x64\x64itionalChannelData\x18\x0c \x01(\x0b\x32\x19.pb.AdditionalChannelData\x12\x11\n\tSubAdFrom\x18\r \x01(\r\x12\x15\n\riQIYIVIPLevel\x18\x0e \x01(\r\x12.\n\x10GamePromoterInfo\x18\x0f \x01(\x0b\x32\x14.pb.GamePromoterInfo\"\xee\x01\n\x0cLoginGameRes\x12\x1c\n\x07ResBase\x18\x01 \x01(\x0b\x32\x0b.pb.ResBase\x12\x12\n\nServerTime\x18\x02 \x01(\r\x12\x1e\n\x08GameData\x18\x03 \x01(\x0b\x32\x0c.pb.GameData\x12\x1e\n\x08GameStat\x18\x04 \x01(\x0b\x32\x0c.pb.GameStat\x12\x18\n\x05Match\x18\x05 \x01(\x0b\x32\t.pb.Match\x12\x12\n\nLoginTimes\x18\x06 \x01(\r\x12\x0e\n\x06GameID\x18\x07 \x01(\r\x12.\n\x10OnlineGameConfig\x18\x08 \x01(\x0b\x32\x14.pb.OnlineGameConfig\"\x83\x01\n\x13LoginGameDataNotify\x12\x12\n\nServerTime\x18\x01 \x01(\r\x12\x1e\n\x08GameData\x18\x02 \x01(\x0b\x32\x0c.pb.GameData\x12\x1e\n\x08GameStat\x18\x03 \x01(\x0b\x32\x0c.pb.GameStat\x12\x18\n\x05Match\x18\x04 \x01(\x0b\x32\t.pb.Match\")\n\x17\x44ifferentLocLoginNotify\x12\x0e\n\x06GameID\x18\x01 \x01(\r\"$\n\x12GetSignInRewardReq\x12\x0e\n\x06GameID\x18\x01 \x01(\r\"\xa8\x01\n\x12GetSignInRewardRes\x12\x1c\n\x07ResBase\x18\x01 \x01(\x0b\x32\x0b.pb.ResBase\x12\x14\n\x0c\x43ontinueDays\x18\x02 \x01(\r\x12\x17\n\x0fMonthSignInDays\x18\x03 \x01(\r\x12\x1a\n\x12LotteryFreeChances\x18\x04 \x01(\r\x12\x13\n\x0b\x44\x61yRewardID\x18\x05 \x01(\r\x12\x14\n\x0c\x44ialRewardID\x18\x06 \x01(\r')
  ,
  dependencies=[UserData_pb2.DESCRIPTOR,GameData_pb2.DESCRIPTOR,Response_pb2.DESCRIPTOR,Match_pb2.DESCRIPTOR,CommonDef_pb2.DESCRIPTOR,CSCommon_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LOGINGAMEREQ = _descriptor.Descriptor(
  name='LoginGameReq',
  full_name='pb.LoginGameReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ChannelData', full_name='pb.LoginGameReq.ChannelData', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BaseData', full_name='pb.LoginGameReq.BaseData', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SceneType', full_name='pb.LoginGameReq.SceneType', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Version', full_name='pb.LoginGameReq.Version', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Cookie', full_name='pb.LoginGameReq.Cookie', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Platform', full_name='pb.LoginGameReq.Platform', index=5,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Device', full_name='pb.LoginGameReq.Device', index=6,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AppType', full_name='pb.LoginGameReq.AppType', index=7,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AdFrom', full_name='pb.LoginGameReq.AdFrom', index=8,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FromAnotherServer', full_name='pb.LoginGameReq.FromAnotherServer', index=9,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AdditionalChannelData', full_name='pb.LoginGameReq.AdditionalChannelData', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SubAdFrom', full_name='pb.LoginGameReq.SubAdFrom', index=11,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iQIYIVIPLevel', full_name='pb.LoginGameReq.iQIYIVIPLevel', index=12,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GamePromoterInfo', full_name='pb.LoginGameReq.GamePromoterInfo', index=13,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=533,
)


_LOGINGAMERES = _descriptor.Descriptor(
  name='LoginGameRes',
  full_name='pb.LoginGameRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ResBase', full_name='pb.LoginGameRes.ResBase', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ServerTime', full_name='pb.LoginGameRes.ServerTime', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GameData', full_name='pb.LoginGameRes.GameData', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GameStat', full_name='pb.LoginGameRes.GameStat', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Match', full_name='pb.LoginGameRes.Match', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LoginTimes', full_name='pb.LoginGameRes.LoginTimes', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GameID', full_name='pb.LoginGameRes.GameID', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OnlineGameConfig', full_name='pb.LoginGameRes.OnlineGameConfig', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=536,
  serialized_end=774,
)


_LOGINGAMEDATANOTIFY = _descriptor.Descriptor(
  name='LoginGameDataNotify',
  full_name='pb.LoginGameDataNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ServerTime', full_name='pb.LoginGameDataNotify.ServerTime', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GameData', full_name='pb.LoginGameDataNotify.GameData', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GameStat', full_name='pb.LoginGameDataNotify.GameStat', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Match', full_name='pb.LoginGameDataNotify.Match', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=777,
  serialized_end=908,
)


_DIFFERENTLOCLOGINNOTIFY = _descriptor.Descriptor(
  name='DifferentLocLoginNotify',
  full_name='pb.DifferentLocLoginNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='GameID', full_name='pb.DifferentLocLoginNotify.GameID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=910,
  serialized_end=951,
)


_GETSIGNINREWARDREQ = _descriptor.Descriptor(
  name='GetSignInRewardReq',
  full_name='pb.GetSignInRewardReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='GameID', full_name='pb.GetSignInRewardReq.GameID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=953,
  serialized_end=989,
)


_GETSIGNINREWARDRES = _descriptor.Descriptor(
  name='GetSignInRewardRes',
  full_name='pb.GetSignInRewardRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ResBase', full_name='pb.GetSignInRewardRes.ResBase', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ContinueDays', full_name='pb.GetSignInRewardRes.ContinueDays', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MonthSignInDays', full_name='pb.GetSignInRewardRes.MonthSignInDays', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LotteryFreeChances', full_name='pb.GetSignInRewardRes.LotteryFreeChances', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DayRewardID', full_name='pb.GetSignInRewardRes.DayRewardID', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DialRewardID', full_name='pb.GetSignInRewardRes.DialRewardID', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=992,
  serialized_end=1160,
)

_LOGINGAMEREQ.fields_by_name['ChannelData'].message_type = GameData_pb2._CHANNELDATA
_LOGINGAMEREQ.fields_by_name['BaseData'].message_type = GameData_pb2._BASEDATA
_LOGINGAMEREQ.fields_by_name['Platform'].enum_type = CommonDef_pb2._PLATFORM
_LOGINGAMEREQ.fields_by_name['Device'].enum_type = CommonDef_pb2._DEVICE
_LOGINGAMEREQ.fields_by_name['AppType'].enum_type = CommonDef_pb2._APPTYPE
_LOGINGAMEREQ.fields_by_name['AdditionalChannelData'].message_type = UserData_pb2._ADDITIONALCHANNELDATA
_LOGINGAMEREQ.fields_by_name['GamePromoterInfo'].message_type = GameData_pb2._GAMEPROMOTERINFO
_LOGINGAMERES.fields_by_name['ResBase'].message_type = Response_pb2._RESBASE
_LOGINGAMERES.fields_by_name['GameData'].message_type = GameData_pb2._GAMEDATA
_LOGINGAMERES.fields_by_name['GameStat'].message_type = GameData_pb2._GAMESTAT
_LOGINGAMERES.fields_by_name['Match'].message_type = Match_pb2._MATCH
_LOGINGAMERES.fields_by_name['OnlineGameConfig'].message_type = CSCommon_pb2._ONLINEGAMECONFIG
_LOGINGAMEDATANOTIFY.fields_by_name['GameData'].message_type = GameData_pb2._GAMEDATA
_LOGINGAMEDATANOTIFY.fields_by_name['GameStat'].message_type = GameData_pb2._GAMESTAT
_LOGINGAMEDATANOTIFY.fields_by_name['Match'].message_type = Match_pb2._MATCH
_GETSIGNINREWARDRES.fields_by_name['ResBase'].message_type = Response_pb2._RESBASE
DESCRIPTOR.message_types_by_name['LoginGameReq'] = _LOGINGAMEREQ
DESCRIPTOR.message_types_by_name['LoginGameRes'] = _LOGINGAMERES
DESCRIPTOR.message_types_by_name['LoginGameDataNotify'] = _LOGINGAMEDATANOTIFY
DESCRIPTOR.message_types_by_name['DifferentLocLoginNotify'] = _DIFFERENTLOCLOGINNOTIFY
DESCRIPTOR.message_types_by_name['GetSignInRewardReq'] = _GETSIGNINREWARDREQ
DESCRIPTOR.message_types_by_name['GetSignInRewardRes'] = _GETSIGNINREWARDRES

LoginGameReq = _reflection.GeneratedProtocolMessageType('LoginGameReq', (_message.Message,), dict(
  DESCRIPTOR = _LOGINGAMEREQ,
  __module__ = 'CSLogin_pb2'
  # @@protoc_insertion_point(class_scope:pb.LoginGameReq)
  ))
_sym_db.RegisterMessage(LoginGameReq)

LoginGameRes = _reflection.GeneratedProtocolMessageType('LoginGameRes', (_message.Message,), dict(
  DESCRIPTOR = _LOGINGAMERES,
  __module__ = 'CSLogin_pb2'
  # @@protoc_insertion_point(class_scope:pb.LoginGameRes)
  ))
_sym_db.RegisterMessage(LoginGameRes)

LoginGameDataNotify = _reflection.GeneratedProtocolMessageType('LoginGameDataNotify', (_message.Message,), dict(
  DESCRIPTOR = _LOGINGAMEDATANOTIFY,
  __module__ = 'CSLogin_pb2'
  # @@protoc_insertion_point(class_scope:pb.LoginGameDataNotify)
  ))
_sym_db.RegisterMessage(LoginGameDataNotify)

DifferentLocLoginNotify = _reflection.GeneratedProtocolMessageType('DifferentLocLoginNotify', (_message.Message,), dict(
  DESCRIPTOR = _DIFFERENTLOCLOGINNOTIFY,
  __module__ = 'CSLogin_pb2'
  # @@protoc_insertion_point(class_scope:pb.DifferentLocLoginNotify)
  ))
_sym_db.RegisterMessage(DifferentLocLoginNotify)

GetSignInRewardReq = _reflection.GeneratedProtocolMessageType('GetSignInRewardReq', (_message.Message,), dict(
  DESCRIPTOR = _GETSIGNINREWARDREQ,
  __module__ = 'CSLogin_pb2'
  # @@protoc_insertion_point(class_scope:pb.GetSignInRewardReq)
  ))
_sym_db.RegisterMessage(GetSignInRewardReq)

GetSignInRewardRes = _reflection.GeneratedProtocolMessageType('GetSignInRewardRes', (_message.Message,), dict(
  DESCRIPTOR = _GETSIGNINREWARDRES,
  __module__ = 'CSLogin_pb2'
  # @@protoc_insertion_point(class_scope:pb.GetSignInRewardRes)
  ))
_sym_db.RegisterMessage(GetSignInRewardRes)


# @@protoc_insertion_point(module_scope)
