# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SSSDK.proto

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
import CSPay_pb2
import CommonDef_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='SSSDK.proto',
  package='pb',
  serialized_pb=_b('\n\x0bSSSDK.proto\x12\x02pb\x1a\x0eResponse.proto\x1a\x0b\x43SPay.proto\x1a\x0f\x43ommonDef.proto\"z\n\x12\x43hannelPaymentData\x12\x13\n\x0b\x43hannelType\x18\x01 \x01(\r\x12\x11\n\tChannelID\x18\x02 \x01(\t\x12\x13\n\x0bProductName\x18\x03 \x01(\t\x12\x13\n\x0bProductDesc\x18\x04 \x01(\t\x12\x12\n\nSDKVersion\x18\x05 \x01(\r\"n\n\rSSLoginSDKReq\x12\x13\n\x0b\x43hannelType\x18\x01 \x01(\r\x12\x11\n\tChannelID\x18\x02 \x01(\t\x12\x11\n\tAuthToken\x18\x03 \x01(\t\x12\x0e\n\x06GameID\x18\x04 \x01(\r\x12\x12\n\nSDKRawData\x18\x05 \x01(\t\"t\n\rSSLoginSDKRes\x12\x1c\n\x07ResBase\x18\x01 \x01(\x0b\x32\x0b.pb.ResBase\x12\x11\n\tChannelID\x18\x02 \x01(\t\x12\x0c\n\x04Nick\x18\x03 \x01(\t\x12\x14\n\x03Sex\x18\x04 \x01(\x0e\x32\x07.pb.Sex\x12\x0e\n\x06\x41vatar\x18\x05 \x01(\t\"\x86\x01\n\x0bSSPaySDKReq\x12$\n\x0bPaymentData\x18\x01 \x01(\x0b\x32\x0f.pb.PaymentData\x12\x32\n\x12\x43hannelPaymentData\x18\x02 \x01(\x0b\x32\x16.pb.ChannelPaymentData\x12\x0f\n\x07OrderID\x18\x03 \x01(\x04\x12\x0c\n\x04Time\x18\x04 \x01(\r\"V\n\x0bSSPaySDKRes\x12\x1c\n\x07ResBase\x18\x01 \x01(\x0b\x32\x0b.pb.ResBase\x12\x14\n\x0c\x43hannelOrder\x18\x02 \x01(\t\x12\x13\n\x0b\x43hannelData\x18\x03 \x01(\t')
  ,
  dependencies=[Response_pb2.DESCRIPTOR,CSPay_pb2.DESCRIPTOR,CommonDef_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHANNELPAYMENTDATA = _descriptor.Descriptor(
  name='ChannelPaymentData',
  full_name='pb.ChannelPaymentData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ChannelType', full_name='pb.ChannelPaymentData.ChannelType', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ChannelID', full_name='pb.ChannelPaymentData.ChannelID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ProductName', full_name='pb.ChannelPaymentData.ProductName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ProductDesc', full_name='pb.ChannelPaymentData.ProductDesc', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SDKVersion', full_name='pb.ChannelPaymentData.SDKVersion', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=65,
  serialized_end=187,
)


_SSLOGINSDKREQ = _descriptor.Descriptor(
  name='SSLoginSDKReq',
  full_name='pb.SSLoginSDKReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ChannelType', full_name='pb.SSLoginSDKReq.ChannelType', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ChannelID', full_name='pb.SSLoginSDKReq.ChannelID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AuthToken', full_name='pb.SSLoginSDKReq.AuthToken', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GameID', full_name='pb.SSLoginSDKReq.GameID', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SDKRawData', full_name='pb.SSLoginSDKReq.SDKRawData', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=189,
  serialized_end=299,
)


_SSLOGINSDKRES = _descriptor.Descriptor(
  name='SSLoginSDKRes',
  full_name='pb.SSLoginSDKRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ResBase', full_name='pb.SSLoginSDKRes.ResBase', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ChannelID', full_name='pb.SSLoginSDKRes.ChannelID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Nick', full_name='pb.SSLoginSDKRes.Nick', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Sex', full_name='pb.SSLoginSDKRes.Sex', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Avatar', full_name='pb.SSLoginSDKRes.Avatar', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=301,
  serialized_end=417,
)


_SSPAYSDKREQ = _descriptor.Descriptor(
  name='SSPaySDKReq',
  full_name='pb.SSPaySDKReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PaymentData', full_name='pb.SSPaySDKReq.PaymentData', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ChannelPaymentData', full_name='pb.SSPaySDKReq.ChannelPaymentData', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OrderID', full_name='pb.SSPaySDKReq.OrderID', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Time', full_name='pb.SSPaySDKReq.Time', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=420,
  serialized_end=554,
)


_SSPAYSDKRES = _descriptor.Descriptor(
  name='SSPaySDKRes',
  full_name='pb.SSPaySDKRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ResBase', full_name='pb.SSPaySDKRes.ResBase', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ChannelOrder', full_name='pb.SSPaySDKRes.ChannelOrder', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ChannelData', full_name='pb.SSPaySDKRes.ChannelData', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=556,
  serialized_end=642,
)

_SSLOGINSDKRES.fields_by_name['ResBase'].message_type = Response_pb2._RESBASE
_SSLOGINSDKRES.fields_by_name['Sex'].enum_type = CommonDef_pb2._SEX
_SSPAYSDKREQ.fields_by_name['PaymentData'].message_type = CSPay_pb2._PAYMENTDATA
_SSPAYSDKREQ.fields_by_name['ChannelPaymentData'].message_type = _CHANNELPAYMENTDATA
_SSPAYSDKRES.fields_by_name['ResBase'].message_type = Response_pb2._RESBASE
DESCRIPTOR.message_types_by_name['ChannelPaymentData'] = _CHANNELPAYMENTDATA
DESCRIPTOR.message_types_by_name['SSLoginSDKReq'] = _SSLOGINSDKREQ
DESCRIPTOR.message_types_by_name['SSLoginSDKRes'] = _SSLOGINSDKRES
DESCRIPTOR.message_types_by_name['SSPaySDKReq'] = _SSPAYSDKREQ
DESCRIPTOR.message_types_by_name['SSPaySDKRes'] = _SSPAYSDKRES

ChannelPaymentData = _reflection.GeneratedProtocolMessageType('ChannelPaymentData', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELPAYMENTDATA,
  __module__ = 'SSSDK_pb2'
  # @@protoc_insertion_point(class_scope:pb.ChannelPaymentData)
  ))
_sym_db.RegisterMessage(ChannelPaymentData)

SSLoginSDKReq = _reflection.GeneratedProtocolMessageType('SSLoginSDKReq', (_message.Message,), dict(
  DESCRIPTOR = _SSLOGINSDKREQ,
  __module__ = 'SSSDK_pb2'
  # @@protoc_insertion_point(class_scope:pb.SSLoginSDKReq)
  ))
_sym_db.RegisterMessage(SSLoginSDKReq)

SSLoginSDKRes = _reflection.GeneratedProtocolMessageType('SSLoginSDKRes', (_message.Message,), dict(
  DESCRIPTOR = _SSLOGINSDKRES,
  __module__ = 'SSSDK_pb2'
  # @@protoc_insertion_point(class_scope:pb.SSLoginSDKRes)
  ))
_sym_db.RegisterMessage(SSLoginSDKRes)

SSPaySDKReq = _reflection.GeneratedProtocolMessageType('SSPaySDKReq', (_message.Message,), dict(
  DESCRIPTOR = _SSPAYSDKREQ,
  __module__ = 'SSSDK_pb2'
  # @@protoc_insertion_point(class_scope:pb.SSPaySDKReq)
  ))
_sym_db.RegisterMessage(SSPaySDKReq)

SSPaySDKRes = _reflection.GeneratedProtocolMessageType('SSPaySDKRes', (_message.Message,), dict(
  DESCRIPTOR = _SSPAYSDKRES,
  __module__ = 'SSSDK_pb2'
  # @@protoc_insertion_point(class_scope:pb.SSPaySDKRes)
  ))
_sym_db.RegisterMessage(SSPaySDKRes)


# @@protoc_insertion_point(module_scope)
