# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PlatformCommon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='PlatformCommon.proto',
  package='pb.platform',
  serialized_pb=_b('\n\x14PlatformCommon.proto\x12\x0bpb.platform\"\x83\x01\n\x0e\x45\x42RedeemStatus\x12\x12\n\nPropertyID\x18\x01 \x01(\r\x12\x11\n\tPackageID\x18\x02 \x01(\x04\x12\x12\n\nRedeemTime\x18\x03 \x01(\r\x12\x13\n\x0b\x44\x65liverTime\x18\x04 \x01(\t\x12\x11\n\tExpressID\x18\x05 \x01(\t\x12\x0e\n\x06Status\x18\x06 \x01(\t\"+\n\rEBAddressData\x12\x0c\n\x04\x43ode\x18\x01 \x01(\r\x12\x0c\n\x04Name\x18\x02 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EBREDEEMSTATUS = _descriptor.Descriptor(
  name='EBRedeemStatus',
  full_name='pb.platform.EBRedeemStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PropertyID', full_name='pb.platform.EBRedeemStatus.PropertyID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PackageID', full_name='pb.platform.EBRedeemStatus.PackageID', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RedeemTime', full_name='pb.platform.EBRedeemStatus.RedeemTime', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DeliverTime', full_name='pb.platform.EBRedeemStatus.DeliverTime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ExpressID', full_name='pb.platform.EBRedeemStatus.ExpressID', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Status', full_name='pb.platform.EBRedeemStatus.Status', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=38,
  serialized_end=169,
)


_EBADDRESSDATA = _descriptor.Descriptor(
  name='EBAddressData',
  full_name='pb.platform.EBAddressData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Code', full_name='pb.platform.EBAddressData.Code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Name', full_name='pb.platform.EBAddressData.Name', index=1,
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
  serialized_start=171,
  serialized_end=214,
)

DESCRIPTOR.message_types_by_name['EBRedeemStatus'] = _EBREDEEMSTATUS
DESCRIPTOR.message_types_by_name['EBAddressData'] = _EBADDRESSDATA

EBRedeemStatus = _reflection.GeneratedProtocolMessageType('EBRedeemStatus', (_message.Message,), dict(
  DESCRIPTOR = _EBREDEEMSTATUS,
  __module__ = 'PlatformCommon_pb2'
  # @@protoc_insertion_point(class_scope:pb.platform.EBRedeemStatus)
  ))
_sym_db.RegisterMessage(EBRedeemStatus)

EBAddressData = _reflection.GeneratedProtocolMessageType('EBAddressData', (_message.Message,), dict(
  DESCRIPTOR = _EBADDRESSDATA,
  __module__ = 'PlatformCommon_pb2'
  # @@protoc_insertion_point(class_scope:pb.platform.EBAddressData)
  ))
_sym_db.RegisterMessage(EBAddressData)


# @@protoc_insertion_point(module_scope)