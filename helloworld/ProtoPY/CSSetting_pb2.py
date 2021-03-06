# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CSSetting.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Response_pb2
import GameData_pb2
import CommonDef_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='CSSetting.proto',
  package='pb',
  serialized_pb=_b('\n\x0f\x43SSetting.proto\x12\x02pb\x1a\x0eResponse.proto\x1a\x0eGameData.proto\x1a\x0f\x43ommonDef.proto\"%\n\x11\x43hangeSettingsReq\x12\x10\n\x08Settings\x18\x01 \x01(\t\"1\n\x11\x43hangeSettingsRes\x12\x1c\n\x07ResBase\x18\x01 \x01(\x0b\x32\x0b.pb.ResBase\"3\n\x13\x43hangePlayerNickReq\x12\x0e\n\x06UserID\x18\x01 \x01(\r\x12\x0c\n\x04Nick\x18\x02 \x01(\t\"\x95\x01\n\x13\x43hangePlayerNickRes\x12\x1c\n\x07ResBase\x18\x01 \x01(\x0b\x32\x0b.pb.ResBase\x12\x1e\n\x08\x42\x61seData\x18\x02 \x01(\x0b\x32\x0c.pb.BaseData\x12\x1e\n\x08\x43oreData\x18\x03 \x01(\x0b\x32\x0c.pb.CoreData\x12 \n\tTrackData\x18\x04 \x01(\x0b\x32\r.pb.TrackData\"7\n\x15\x43hangePlayerRoleIDReq\x12\x0e\n\x06UserID\x18\x01 \x01(\r\x12\x0e\n\x06RoleID\x18\x02 \x01(\r\"\xb9\x01\n\x15\x43hangePlayerRoleIDRes\x12\x1c\n\x07ResBase\x18\x01 \x01(\x0b\x32\x0b.pb.ResBase\x12\x1e\n\x08\x42\x61seData\x18\x02 \x01(\x0b\x32\x0c.pb.BaseData\x12\x1e\n\x08\x43oreData\x18\x03 \x01(\x0b\x32\x0c.pb.CoreData\x12 \n\tTrackData\x18\x04 \x01(\x0b\x32\r.pb.TrackData\x12 \n\tExtraData\x18\x05 \x01(\x0b\x32\r.pb.ExtraData\":\n\x12\x43hangePlayerSexReq\x12\x0e\n\x06UserID\x18\x01 \x01(\r\x12\x14\n\x03Sex\x18\x02 \x01(\x0e\x32\x07.pb.Sex\"R\n\x12\x43hangePlayerSexRes\x12\x1c\n\x07ResBase\x18\x01 \x01(\x0b\x32\x0b.pb.ResBase\x12\x1e\n\x08\x42\x61seData\x18\x02 \x01(\x0b\x32\x0c.pb.BaseData\"9\n\x11SetPrivateDataReq\x12$\n\x0bPrivateData\x18\x01 \x01(\x0b\x32\x0f.pb.PrivateData\"1\n\x11SetPrivateDataRes\x12\x1c\n\x07ResBase\x18\x01 \x01(\x0b\x32\x0b.pb.ResBase\"\x13\n\x11GetPrivateDataReq\"W\n\x11GetPrivateDataRes\x12\x1c\n\x07ResBase\x18\x01 \x01(\x0b\x32\x0b.pb.ResBase\x12$\n\x0bPrivateData\x18\x02 \x01(\x0b\x32\x0f.pb.PrivateData')
  ,
  dependencies=[Response_pb2.DESCRIPTOR,GameData_pb2.DESCRIPTOR,CommonDef_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHANGESETTINGSREQ = _descriptor.Descriptor(
  name='ChangeSettingsReq',
  full_name='pb.ChangeSettingsReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Settings', full_name='pb.ChangeSettingsReq.Settings', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=72,
  serialized_end=109,
)


_CHANGESETTINGSRES = _descriptor.Descriptor(
  name='ChangeSettingsRes',
  full_name='pb.ChangeSettingsRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ResBase', full_name='pb.ChangeSettingsRes.ResBase', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=111,
  serialized_end=160,
)


_CHANGEPLAYERNICKREQ = _descriptor.Descriptor(
  name='ChangePlayerNickReq',
  full_name='pb.ChangePlayerNickReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='UserID', full_name='pb.ChangePlayerNickReq.UserID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Nick', full_name='pb.ChangePlayerNickReq.Nick', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=162,
  serialized_end=213,
)


_CHANGEPLAYERNICKRES = _descriptor.Descriptor(
  name='ChangePlayerNickRes',
  full_name='pb.ChangePlayerNickRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ResBase', full_name='pb.ChangePlayerNickRes.ResBase', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BaseData', full_name='pb.ChangePlayerNickRes.BaseData', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CoreData', full_name='pb.ChangePlayerNickRes.CoreData', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TrackData', full_name='pb.ChangePlayerNickRes.TrackData', index=3,
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
  serialized_start=216,
  serialized_end=365,
)


_CHANGEPLAYERROLEIDREQ = _descriptor.Descriptor(
  name='ChangePlayerRoleIDReq',
  full_name='pb.ChangePlayerRoleIDReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='UserID', full_name='pb.ChangePlayerRoleIDReq.UserID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RoleID', full_name='pb.ChangePlayerRoleIDReq.RoleID', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=367,
  serialized_end=422,
)


_CHANGEPLAYERROLEIDRES = _descriptor.Descriptor(
  name='ChangePlayerRoleIDRes',
  full_name='pb.ChangePlayerRoleIDRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ResBase', full_name='pb.ChangePlayerRoleIDRes.ResBase', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BaseData', full_name='pb.ChangePlayerRoleIDRes.BaseData', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CoreData', full_name='pb.ChangePlayerRoleIDRes.CoreData', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TrackData', full_name='pb.ChangePlayerRoleIDRes.TrackData', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ExtraData', full_name='pb.ChangePlayerRoleIDRes.ExtraData', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=425,
  serialized_end=610,
)


_CHANGEPLAYERSEXREQ = _descriptor.Descriptor(
  name='ChangePlayerSexReq',
  full_name='pb.ChangePlayerSexReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='UserID', full_name='pb.ChangePlayerSexReq.UserID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Sex', full_name='pb.ChangePlayerSexReq.Sex', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=612,
  serialized_end=670,
)


_CHANGEPLAYERSEXRES = _descriptor.Descriptor(
  name='ChangePlayerSexRes',
  full_name='pb.ChangePlayerSexRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ResBase', full_name='pb.ChangePlayerSexRes.ResBase', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BaseData', full_name='pb.ChangePlayerSexRes.BaseData', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=672,
  serialized_end=754,
)


_SETPRIVATEDATAREQ = _descriptor.Descriptor(
  name='SetPrivateDataReq',
  full_name='pb.SetPrivateDataReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PrivateData', full_name='pb.SetPrivateDataReq.PrivateData', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=756,
  serialized_end=813,
)


_SETPRIVATEDATARES = _descriptor.Descriptor(
  name='SetPrivateDataRes',
  full_name='pb.SetPrivateDataRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ResBase', full_name='pb.SetPrivateDataRes.ResBase', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=815,
  serialized_end=864,
)


_GETPRIVATEDATAREQ = _descriptor.Descriptor(
  name='GetPrivateDataReq',
  full_name='pb.GetPrivateDataReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=866,
  serialized_end=885,
)


_GETPRIVATEDATARES = _descriptor.Descriptor(
  name='GetPrivateDataRes',
  full_name='pb.GetPrivateDataRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ResBase', full_name='pb.GetPrivateDataRes.ResBase', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PrivateData', full_name='pb.GetPrivateDataRes.PrivateData', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=887,
  serialized_end=974,
)

_CHANGESETTINGSRES.fields_by_name['ResBase'].message_type = Response_pb2._RESBASE
_CHANGEPLAYERNICKRES.fields_by_name['ResBase'].message_type = Response_pb2._RESBASE
_CHANGEPLAYERNICKRES.fields_by_name['BaseData'].message_type = GameData_pb2._BASEDATA
_CHANGEPLAYERNICKRES.fields_by_name['CoreData'].message_type = GameData_pb2._COREDATA
_CHANGEPLAYERNICKRES.fields_by_name['TrackData'].message_type = GameData_pb2._TRACKDATA
_CHANGEPLAYERROLEIDRES.fields_by_name['ResBase'].message_type = Response_pb2._RESBASE
_CHANGEPLAYERROLEIDRES.fields_by_name['BaseData'].message_type = GameData_pb2._BASEDATA
_CHANGEPLAYERROLEIDRES.fields_by_name['CoreData'].message_type = GameData_pb2._COREDATA
_CHANGEPLAYERROLEIDRES.fields_by_name['TrackData'].message_type = GameData_pb2._TRACKDATA
_CHANGEPLAYERROLEIDRES.fields_by_name['ExtraData'].message_type = GameData_pb2._EXTRADATA
_CHANGEPLAYERSEXREQ.fields_by_name['Sex'].enum_type = CommonDef_pb2._SEX
_CHANGEPLAYERSEXRES.fields_by_name['ResBase'].message_type = Response_pb2._RESBASE
_CHANGEPLAYERSEXRES.fields_by_name['BaseData'].message_type = GameData_pb2._BASEDATA
_SETPRIVATEDATAREQ.fields_by_name['PrivateData'].message_type = GameData_pb2._PRIVATEDATA
_SETPRIVATEDATARES.fields_by_name['ResBase'].message_type = Response_pb2._RESBASE
_GETPRIVATEDATARES.fields_by_name['ResBase'].message_type = Response_pb2._RESBASE
_GETPRIVATEDATARES.fields_by_name['PrivateData'].message_type = GameData_pb2._PRIVATEDATA
DESCRIPTOR.message_types_by_name['ChangeSettingsReq'] = _CHANGESETTINGSREQ
DESCRIPTOR.message_types_by_name['ChangeSettingsRes'] = _CHANGESETTINGSRES
DESCRIPTOR.message_types_by_name['ChangePlayerNickReq'] = _CHANGEPLAYERNICKREQ
DESCRIPTOR.message_types_by_name['ChangePlayerNickRes'] = _CHANGEPLAYERNICKRES
DESCRIPTOR.message_types_by_name['ChangePlayerRoleIDReq'] = _CHANGEPLAYERROLEIDREQ
DESCRIPTOR.message_types_by_name['ChangePlayerRoleIDRes'] = _CHANGEPLAYERROLEIDRES
DESCRIPTOR.message_types_by_name['ChangePlayerSexReq'] = _CHANGEPLAYERSEXREQ
DESCRIPTOR.message_types_by_name['ChangePlayerSexRes'] = _CHANGEPLAYERSEXRES
DESCRIPTOR.message_types_by_name['SetPrivateDataReq'] = _SETPRIVATEDATAREQ
DESCRIPTOR.message_types_by_name['SetPrivateDataRes'] = _SETPRIVATEDATARES
DESCRIPTOR.message_types_by_name['GetPrivateDataReq'] = _GETPRIVATEDATAREQ
DESCRIPTOR.message_types_by_name['GetPrivateDataRes'] = _GETPRIVATEDATARES

ChangeSettingsReq = _reflection.GeneratedProtocolMessageType('ChangeSettingsReq', (_message.Message,), dict(
  DESCRIPTOR = _CHANGESETTINGSREQ,
  __module__ = 'CSSetting_pb2'
  # @@protoc_insertion_point(class_scope:pb.ChangeSettingsReq)
  ))
_sym_db.RegisterMessage(ChangeSettingsReq)

ChangeSettingsRes = _reflection.GeneratedProtocolMessageType('ChangeSettingsRes', (_message.Message,), dict(
  DESCRIPTOR = _CHANGESETTINGSRES,
  __module__ = 'CSSetting_pb2'
  # @@protoc_insertion_point(class_scope:pb.ChangeSettingsRes)
  ))
_sym_db.RegisterMessage(ChangeSettingsRes)

ChangePlayerNickReq = _reflection.GeneratedProtocolMessageType('ChangePlayerNickReq', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEPLAYERNICKREQ,
  __module__ = 'CSSetting_pb2'
  # @@protoc_insertion_point(class_scope:pb.ChangePlayerNickReq)
  ))
_sym_db.RegisterMessage(ChangePlayerNickReq)

ChangePlayerNickRes = _reflection.GeneratedProtocolMessageType('ChangePlayerNickRes', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEPLAYERNICKRES,
  __module__ = 'CSSetting_pb2'
  # @@protoc_insertion_point(class_scope:pb.ChangePlayerNickRes)
  ))
_sym_db.RegisterMessage(ChangePlayerNickRes)

ChangePlayerRoleIDReq = _reflection.GeneratedProtocolMessageType('ChangePlayerRoleIDReq', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEPLAYERROLEIDREQ,
  __module__ = 'CSSetting_pb2'
  # @@protoc_insertion_point(class_scope:pb.ChangePlayerRoleIDReq)
  ))
_sym_db.RegisterMessage(ChangePlayerRoleIDReq)

ChangePlayerRoleIDRes = _reflection.GeneratedProtocolMessageType('ChangePlayerRoleIDRes', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEPLAYERROLEIDRES,
  __module__ = 'CSSetting_pb2'
  # @@protoc_insertion_point(class_scope:pb.ChangePlayerRoleIDRes)
  ))
_sym_db.RegisterMessage(ChangePlayerRoleIDRes)

ChangePlayerSexReq = _reflection.GeneratedProtocolMessageType('ChangePlayerSexReq', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEPLAYERSEXREQ,
  __module__ = 'CSSetting_pb2'
  # @@protoc_insertion_point(class_scope:pb.ChangePlayerSexReq)
  ))
_sym_db.RegisterMessage(ChangePlayerSexReq)

ChangePlayerSexRes = _reflection.GeneratedProtocolMessageType('ChangePlayerSexRes', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEPLAYERSEXRES,
  __module__ = 'CSSetting_pb2'
  # @@protoc_insertion_point(class_scope:pb.ChangePlayerSexRes)
  ))
_sym_db.RegisterMessage(ChangePlayerSexRes)

SetPrivateDataReq = _reflection.GeneratedProtocolMessageType('SetPrivateDataReq', (_message.Message,), dict(
  DESCRIPTOR = _SETPRIVATEDATAREQ,
  __module__ = 'CSSetting_pb2'
  # @@protoc_insertion_point(class_scope:pb.SetPrivateDataReq)
  ))
_sym_db.RegisterMessage(SetPrivateDataReq)

SetPrivateDataRes = _reflection.GeneratedProtocolMessageType('SetPrivateDataRes', (_message.Message,), dict(
  DESCRIPTOR = _SETPRIVATEDATARES,
  __module__ = 'CSSetting_pb2'
  # @@protoc_insertion_point(class_scope:pb.SetPrivateDataRes)
  ))
_sym_db.RegisterMessage(SetPrivateDataRes)

GetPrivateDataReq = _reflection.GeneratedProtocolMessageType('GetPrivateDataReq', (_message.Message,), dict(
  DESCRIPTOR = _GETPRIVATEDATAREQ,
  __module__ = 'CSSetting_pb2'
  # @@protoc_insertion_point(class_scope:pb.GetPrivateDataReq)
  ))
_sym_db.RegisterMessage(GetPrivateDataReq)

GetPrivateDataRes = _reflection.GeneratedProtocolMessageType('GetPrivateDataRes', (_message.Message,), dict(
  DESCRIPTOR = _GETPRIVATEDATARES,
  __module__ = 'CSSetting_pb2'
  # @@protoc_insertion_point(class_scope:pb.GetPrivateDataRes)
  ))
_sym_db.RegisterMessage(GetPrivateDataRes)


# @@protoc_insertion_point(module_scope)
