# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CommonDef.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='CommonDef.proto',
  package='pb',
  serialized_pb=_b('\n\x0f\x43ommonDef.proto\x12\x02pb*\x85\x02\n\x0b\x43hannelType\x12\x0c\n\x08\x43T_QIBAI\x10\x00\x12\x0c\n\x08\x43T_IQIYI\x10\x01\x12\x0c\n\x08\x43T_ROBOT\x10\x02\x12\x0b\n\x07\x43T_OPPO\x10\x03\x12\x0b\n\x07\x43T_VIVO\x10\x04\x12\r\n\tCT_HUAWEI\x10\x05\x12\r\n\tCT_XIAOMI\x10\x06\x12\x0c\n\x08\x43T_BAIDU\x10\x07\x12\x11\n\rCT_TENCENTAPP\x10\x08\x12\t\n\x05\x43T_UC\x10\t\x12\n\n\x06\x43T_360\x10\n\x12\r\n\tCT_LENOVO\x10\x0b\x12\r\n\tCT_GIONEE\x10\x0c\x12\x0e\n\nCT_COOLPAD\x10\r\x12\x0c\n\x08\x43T_MEIZU\x10\x0e\x12\x10\n\x0c\x43T_MINIGAMES\x10\x0f\x12\x0e\n\nCT_WIFIKEY\x10\x10**\n\x03Sex\x12\r\n\tUNDEFINED\x10\x00\x12\x08\n\x04MALE\x10\x01\x12\n\n\x06\x46\x45MALE\x10\x02*\xf1\x05\n\x0cPropertyType\x12\x17\n\x13PROPERTY_GAME_MONEY\x10\x01\x12\x14\n\x10PROPERTY_DIAMOND\x10\x02\x12\x1b\n\x17PROPERTY_TELEPHONE_FARE\x10\x03\x12\x13\n\x0fPROPERTY_TICKET\x10\x04\x12\x18\n\x14PROPERTY_OBJECT_CARD\x10\x05\x12\x1c\n\x18PROPERTY_GAME_MONEY_CARD\x10\n\x12\x17\n\x13PROPERTY_CHARM_CARD\x10\x0b\x12\x15\n\x11PROPERTY_EXP_CARD\x10\x0c\x12\x18\n\x14PROPERTY_BACK_GROUND\x10\x0e\x12\x1c\n\x18PROPERTY_RANDOM_TREASURE\x10\x0f\x12\x1c\n\x18PROPERTY_EXCHANGE_TICKET\x10\x10\x12\x11\n\rPROPERTY_HEAD\x10\x11\x12\x1d\n\x19PROPERTY_IQIYI_VIP_COUPON\x10\x12\x12\x1b\n\x17PROPERTY_IQIYI_VIP_CODE\x10\x13\x12\x15\n\x11PROPERTY_FRAGMENT\x10\x14\x12\x1a\n\x16PROPERTY_LOTTER_TICKET\x10\x15\x12\x1c\n\x18PROPERTY_IQIYI_VIP_TRIAL\x10\x16\x12$\n PROPERTY_GAMECENTER_GIFT_PACKAGE\x10\x17\x12!\n\x1dPROPERTY_CELLPHONE_FEE_TICKET\x10\x18\x12\x19\n\x15PROPERTY_TREASURE_BOX\x10\x19\x12\x17\n\x13PROPERTY_RED_PACKET\x10\x1a\x12\x14\n\x10PROPERTY_COSTUME\x10\x1b\x12\x11\n\rPROPERTY_GIFT\x10\x1c\x12\x16\n\x12PROPERTY_CHARACTER\x10\x1d\x12\x19\n\x15PROPERTY_WECHAT_1CENT\x10\x1e\x12\x14\n\x10PROPERTY_FORTUNE\x10\x1f\x12\x1b\n\x17PROPERTY_WECHAT_REDPACK\x10 \x12\x16\n\x12PROPERTY_GOLD_BEAN\x10!*_\n\x12GlobalOpResultType\x12\x11\n\rGORT_UNDEFINE\x10\x00\x12\x18\n\x14GORT_REGISTER_ONLINE\x10\x01\x12\r\n\tGORT_SUCC\x10\x02\x12\r\n\tGORT_FAIL\x10\x03*^\n\x08Platform\x12\x14\n\x10PLATFORM_UNKNOWN\x10\x00\x12\x10\n\x0cPLATFORM_IOS\x10\x01\x12\x14\n\x10PLATFORM_ANDROID\x10\x02\x12\x14\n\x10PLATFORM_WINDOWS\x10\x03*_\n\x06\x44\x65vice\x12\x11\n\rDEVICE_UNKOWN\x10\x00\x12\r\n\tDEVICE_PC\x10\x01\x12\x11\n\rDEVICE_MOBILE\x10\x02\x12\x11\n\rDEVICE_TABLET\x10\x03\x12\r\n\tDEVICE_TV\x10\x04*O\n\x07\x41ppType\x12\x10\n\x0c\x41PPTYPE_HTML\x10\x00\x12\x12\n\x0e\x41PPTYPE_NATIVE\x10\x01\x12\x0e\n\nAPPTYPE_TV\x10\x02\x12\x0e\n\nAPPTYPE_PC\x10\x03*\xa5\x02\n\x0e\x44\x65viceCategory\x12\x19\n\x15\x44\x45VICECATEGORY_UNKOWN\x10\x00\x12\x1b\n\x17\x44\x45VICECATEGORY_IOS_HTML\x10\x01\x12\x1d\n\x19\x44\x45VICECATEGORY_IOS_NATIVE\x10\x02\x12\x1f\n\x1b\x44\x45VICECATEGORY_ANDROID_HTML\x10\x03\x12!\n\x1d\x44\x45VICECATEGORY_ANDROID_NATIVE\x10\x04\x12\x1a\n\x16\x44\x45VICECATEGORY_WINDOWS\x10\x05\x12\x1d\n\x19\x44\x45VICECATEGORY_ANDROID_TV\x10\x06\x12\x1e\n\x1a\x44\x45VICECATEGORY_IPAD_NATIVE\x10\x07\x12\x1d\n\x19\x44\x45VICECATEGORY_WINDOWS_PC\x10\x08*o\n\nForbidType\x12\r\n\tFT_NORMAL\x10\x01\x12\x0c\n\x08\x46T_CHEAT\x10\x02\x12\x15\n\x11\x46T_DATA_EXCEPTION\x10\x03\x12\x0c\n\x08\x46T_ABUSE\x10\x04\x12\x11\n\rFT_TMP_FREEZE\x10\x05\x12\x0c\n\x08\x46T_OTHER\x10\x06*k\n\nOnlineType\x12\x19\n\x15ONLINE_TYPE_UNDEFINED\x10\x00\x12\x15\n\x11ONLINE_TYPE_LOGIN\x10\x01\x12\x14\n\x10ONLINE_TYPE_GAME\x10\x02\x12\x15\n\x11ONLINE_TYPE_MATCH\x10\x03*~\n\x0eMailSourceType\x12\x0e\n\nMST_SYSTEM\x10\x01\x12\x16\n\x12MST_CGI_GAMECENTER\x10\x02\x12\n\n\x06MST_GM\x10\x03\x12\x10\n\x0cMST_RECHARGE\x10\x04\x12\x13\n\x0fMST_RANk_REWARD\x10\x05\x12\x11\n\rMST_EB_REDEEM\x10\x06*\xb0\x01\n\nServerType\x12\x0b\n\x07ST_GAME\x10\n\x12\x0c\n\x08ST_LOGIN\x10\x0c\x12\r\n\tST_ONLINE\x10\x0e\x12\x0b\n\x07ST_RANK\x10\x0f\x12\x0c\n\x08ST_WORLD\x10\x10\x12\x0f\n\x0bST_GAMERANK\x10\x11\x12\t\n\x05ST_GM\x10\x12\x12\n\n\x06ST_PAY\x10\x13\x12\x16\n\x12ST_GLOBAL_DELIVERY\x10\x1b\x12\x11\n\rST_GAMECENTER\x10\x1e\x12\n\n\x06ST_SDK\x10\"')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CHANNELTYPE = _descriptor.EnumDescriptor(
  name='ChannelType',
  full_name='pb.ChannelType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CT_QIBAI', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_IQIYI', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_ROBOT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_OPPO', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_VIVO', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_HUAWEI', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_XIAOMI', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_BAIDU', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_TENCENTAPP', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_UC', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_360', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_LENOVO', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_GIONEE', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_COOLPAD', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_MEIZU', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_MINIGAMES', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_WIFIKEY', index=16, number=16,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=24,
  serialized_end=285,
)
_sym_db.RegisterEnumDescriptor(_CHANNELTYPE)

ChannelType = enum_type_wrapper.EnumTypeWrapper(_CHANNELTYPE)
_SEX = _descriptor.EnumDescriptor(
  name='Sex',
  full_name='pb.Sex',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MALE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEMALE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=287,
  serialized_end=329,
)
_sym_db.RegisterEnumDescriptor(_SEX)

Sex = enum_type_wrapper.EnumTypeWrapper(_SEX)
_PROPERTYTYPE = _descriptor.EnumDescriptor(
  name='PropertyType',
  full_name='pb.PropertyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_GAME_MONEY', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_DIAMOND', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_TELEPHONE_FARE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_TICKET', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_OBJECT_CARD', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_GAME_MONEY_CARD', index=5, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_CHARM_CARD', index=6, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_EXP_CARD', index=7, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_BACK_GROUND', index=8, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_RANDOM_TREASURE', index=9, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_EXCHANGE_TICKET', index=10, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_HEAD', index=11, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_IQIYI_VIP_COUPON', index=12, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_IQIYI_VIP_CODE', index=13, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_FRAGMENT', index=14, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_LOTTER_TICKET', index=15, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_IQIYI_VIP_TRIAL', index=16, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_GAMECENTER_GIFT_PACKAGE', index=17, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_CELLPHONE_FEE_TICKET', index=18, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_TREASURE_BOX', index=19, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_RED_PACKET', index=20, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_COSTUME', index=21, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_GIFT', index=22, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_CHARACTER', index=23, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_WECHAT_1CENT', index=24, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_FORTUNE', index=25, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_WECHAT_REDPACK', index=26, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY_GOLD_BEAN', index=27, number=33,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=332,
  serialized_end=1085,
)
_sym_db.RegisterEnumDescriptor(_PROPERTYTYPE)

PropertyType = enum_type_wrapper.EnumTypeWrapper(_PROPERTYTYPE)
_GLOBALOPRESULTTYPE = _descriptor.EnumDescriptor(
  name='GlobalOpResultType',
  full_name='pb.GlobalOpResultType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GORT_UNDEFINE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GORT_REGISTER_ONLINE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GORT_SUCC', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GORT_FAIL', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1087,
  serialized_end=1182,
)
_sym_db.RegisterEnumDescriptor(_GLOBALOPRESULTTYPE)

GlobalOpResultType = enum_type_wrapper.EnumTypeWrapper(_GLOBALOPRESULTTYPE)
_PLATFORM = _descriptor.EnumDescriptor(
  name='Platform',
  full_name='pb.Platform',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_IOS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_ANDROID', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_WINDOWS', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1184,
  serialized_end=1278,
)
_sym_db.RegisterEnumDescriptor(_PLATFORM)

Platform = enum_type_wrapper.EnumTypeWrapper(_PLATFORM)
_DEVICE = _descriptor.EnumDescriptor(
  name='Device',
  full_name='pb.Device',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEVICE_UNKOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_PC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_MOBILE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_TABLET', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_TV', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1280,
  serialized_end=1375,
)
_sym_db.RegisterEnumDescriptor(_DEVICE)

Device = enum_type_wrapper.EnumTypeWrapper(_DEVICE)
_APPTYPE = _descriptor.EnumDescriptor(
  name='AppType',
  full_name='pb.AppType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='APPTYPE_HTML', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPTYPE_NATIVE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPTYPE_TV', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPTYPE_PC', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1377,
  serialized_end=1456,
)
_sym_db.RegisterEnumDescriptor(_APPTYPE)

AppType = enum_type_wrapper.EnumTypeWrapper(_APPTYPE)
_DEVICECATEGORY = _descriptor.EnumDescriptor(
  name='DeviceCategory',
  full_name='pb.DeviceCategory',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEVICECATEGORY_UNKOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICECATEGORY_IOS_HTML', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICECATEGORY_IOS_NATIVE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICECATEGORY_ANDROID_HTML', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICECATEGORY_ANDROID_NATIVE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICECATEGORY_WINDOWS', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICECATEGORY_ANDROID_TV', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICECATEGORY_IPAD_NATIVE', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICECATEGORY_WINDOWS_PC', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1459,
  serialized_end=1752,
)
_sym_db.RegisterEnumDescriptor(_DEVICECATEGORY)

DeviceCategory = enum_type_wrapper.EnumTypeWrapper(_DEVICECATEGORY)
_FORBIDTYPE = _descriptor.EnumDescriptor(
  name='ForbidType',
  full_name='pb.ForbidType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FT_NORMAL', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_CHEAT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_DATA_EXCEPTION', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_ABUSE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_TMP_FREEZE', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_OTHER', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1754,
  serialized_end=1865,
)
_sym_db.RegisterEnumDescriptor(_FORBIDTYPE)

ForbidType = enum_type_wrapper.EnumTypeWrapper(_FORBIDTYPE)
_ONLINETYPE = _descriptor.EnumDescriptor(
  name='OnlineType',
  full_name='pb.OnlineType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ONLINE_TYPE_UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONLINE_TYPE_LOGIN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONLINE_TYPE_GAME', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONLINE_TYPE_MATCH', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1867,
  serialized_end=1974,
)
_sym_db.RegisterEnumDescriptor(_ONLINETYPE)

OnlineType = enum_type_wrapper.EnumTypeWrapper(_ONLINETYPE)
_MAILSOURCETYPE = _descriptor.EnumDescriptor(
  name='MailSourceType',
  full_name='pb.MailSourceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MST_SYSTEM', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MST_CGI_GAMECENTER', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MST_GM', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MST_RECHARGE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MST_RANk_REWARD', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MST_EB_REDEEM', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1976,
  serialized_end=2102,
)
_sym_db.RegisterEnumDescriptor(_MAILSOURCETYPE)

MailSourceType = enum_type_wrapper.EnumTypeWrapper(_MAILSOURCETYPE)
_SERVERTYPE = _descriptor.EnumDescriptor(
  name='ServerType',
  full_name='pb.ServerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ST_GAME', index=0, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_LOGIN', index=1, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_ONLINE', index=2, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_RANK', index=3, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_WORLD', index=4, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_GAMERANK', index=5, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_GM', index=6, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_PAY', index=7, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_GLOBAL_DELIVERY', index=8, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_GAMECENTER', index=9, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_SDK', index=10, number=34,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2105,
  serialized_end=2281,
)
_sym_db.RegisterEnumDescriptor(_SERVERTYPE)

ServerType = enum_type_wrapper.EnumTypeWrapper(_SERVERTYPE)
CT_QIBAI = 0
CT_IQIYI = 1
CT_ROBOT = 2
CT_OPPO = 3
CT_VIVO = 4
CT_HUAWEI = 5
CT_XIAOMI = 6
CT_BAIDU = 7
CT_TENCENTAPP = 8
CT_UC = 9
CT_360 = 10
CT_LENOVO = 11
CT_GIONEE = 12
CT_COOLPAD = 13
CT_MEIZU = 14
CT_MINIGAMES = 15
CT_WIFIKEY = 16
UNDEFINED = 0
MALE = 1
FEMALE = 2
PROPERTY_GAME_MONEY = 1
PROPERTY_DIAMOND = 2
PROPERTY_TELEPHONE_FARE = 3
PROPERTY_TICKET = 4
PROPERTY_OBJECT_CARD = 5
PROPERTY_GAME_MONEY_CARD = 10
PROPERTY_CHARM_CARD = 11
PROPERTY_EXP_CARD = 12
PROPERTY_BACK_GROUND = 14
PROPERTY_RANDOM_TREASURE = 15
PROPERTY_EXCHANGE_TICKET = 16
PROPERTY_HEAD = 17
PROPERTY_IQIYI_VIP_COUPON = 18
PROPERTY_IQIYI_VIP_CODE = 19
PROPERTY_FRAGMENT = 20
PROPERTY_LOTTER_TICKET = 21
PROPERTY_IQIYI_VIP_TRIAL = 22
PROPERTY_GAMECENTER_GIFT_PACKAGE = 23
PROPERTY_CELLPHONE_FEE_TICKET = 24
PROPERTY_TREASURE_BOX = 25
PROPERTY_RED_PACKET = 26
PROPERTY_COSTUME = 27
PROPERTY_GIFT = 28
PROPERTY_CHARACTER = 29
PROPERTY_WECHAT_1CENT = 30
PROPERTY_FORTUNE = 31
PROPERTY_WECHAT_REDPACK = 32
PROPERTY_GOLD_BEAN = 33
GORT_UNDEFINE = 0
GORT_REGISTER_ONLINE = 1
GORT_SUCC = 2
GORT_FAIL = 3
PLATFORM_UNKNOWN = 0
PLATFORM_IOS = 1
PLATFORM_ANDROID = 2
PLATFORM_WINDOWS = 3
DEVICE_UNKOWN = 0
DEVICE_PC = 1
DEVICE_MOBILE = 2
DEVICE_TABLET = 3
DEVICE_TV = 4
APPTYPE_HTML = 0
APPTYPE_NATIVE = 1
APPTYPE_TV = 2
APPTYPE_PC = 3
DEVICECATEGORY_UNKOWN = 0
DEVICECATEGORY_IOS_HTML = 1
DEVICECATEGORY_IOS_NATIVE = 2
DEVICECATEGORY_ANDROID_HTML = 3
DEVICECATEGORY_ANDROID_NATIVE = 4
DEVICECATEGORY_WINDOWS = 5
DEVICECATEGORY_ANDROID_TV = 6
DEVICECATEGORY_IPAD_NATIVE = 7
DEVICECATEGORY_WINDOWS_PC = 8
FT_NORMAL = 1
FT_CHEAT = 2
FT_DATA_EXCEPTION = 3
FT_ABUSE = 4
FT_TMP_FREEZE = 5
FT_OTHER = 6
ONLINE_TYPE_UNDEFINED = 0
ONLINE_TYPE_LOGIN = 1
ONLINE_TYPE_GAME = 2
ONLINE_TYPE_MATCH = 3
MST_SYSTEM = 1
MST_CGI_GAMECENTER = 2
MST_GM = 3
MST_RECHARGE = 4
MST_RANk_REWARD = 5
MST_EB_REDEEM = 6
ST_GAME = 10
ST_LOGIN = 12
ST_ONLINE = 14
ST_RANK = 15
ST_WORLD = 16
ST_GAMERANK = 17
ST_GM = 18
ST_PAY = 19
ST_GLOBAL_DELIVERY = 27
ST_GAMECENTER = 30
ST_SDK = 34


DESCRIPTOR.enum_types_by_name['ChannelType'] = _CHANNELTYPE
DESCRIPTOR.enum_types_by_name['Sex'] = _SEX
DESCRIPTOR.enum_types_by_name['PropertyType'] = _PROPERTYTYPE
DESCRIPTOR.enum_types_by_name['GlobalOpResultType'] = _GLOBALOPRESULTTYPE
DESCRIPTOR.enum_types_by_name['Platform'] = _PLATFORM
DESCRIPTOR.enum_types_by_name['Device'] = _DEVICE
DESCRIPTOR.enum_types_by_name['AppType'] = _APPTYPE
DESCRIPTOR.enum_types_by_name['DeviceCategory'] = _DEVICECATEGORY
DESCRIPTOR.enum_types_by_name['ForbidType'] = _FORBIDTYPE
DESCRIPTOR.enum_types_by_name['OnlineType'] = _ONLINETYPE
DESCRIPTOR.enum_types_by_name['MailSourceType'] = _MAILSOURCETYPE
DESCRIPTOR.enum_types_by_name['ServerType'] = _SERVERTYPE


# @@protoc_insertion_point(module_scope)