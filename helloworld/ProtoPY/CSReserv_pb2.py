# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CSReserv.proto

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
  name='CSReserv.proto',
  package='pb.platform',
  serialized_pb=_b('\n\x0e\x43SReserv.proto\x12\x0bpb.platform\":\n\x13\x43SPlatformReservReq\x12#\n\x03\x43MD\x18\x01 \x01(\x0e\x32\x16.pb.platform.CSCMDType\":\n\x13\x43SPlatformReservRes\x12#\n\x03\x43MD\x18\x01 \x01(\x0e\x32\x16.pb.platform.CSCMDType*\x1c\n\tCSCMDType\x12\x0f\n\x0b\x43S_CMD_TEST\x10\x00')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CSCMDTYPE = _descriptor.EnumDescriptor(
  name='CSCMDType',
  full_name='pb.platform.CSCMDType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CS_CMD_TEST', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=151,
  serialized_end=179,
)
_sym_db.RegisterEnumDescriptor(_CSCMDTYPE)

CSCMDType = enum_type_wrapper.EnumTypeWrapper(_CSCMDTYPE)
CS_CMD_TEST = 0



_CSPLATFORMRESERVREQ = _descriptor.Descriptor(
  name='CSPlatformReservReq',
  full_name='pb.platform.CSPlatformReservReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='CMD', full_name='pb.platform.CSPlatformReservReq.CMD', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=31,
  serialized_end=89,
)


_CSPLATFORMRESERVRES = _descriptor.Descriptor(
  name='CSPlatformReservRes',
  full_name='pb.platform.CSPlatformReservRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='CMD', full_name='pb.platform.CSPlatformReservRes.CMD', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=91,
  serialized_end=149,
)

_CSPLATFORMRESERVREQ.fields_by_name['CMD'].enum_type = _CSCMDTYPE
_CSPLATFORMRESERVRES.fields_by_name['CMD'].enum_type = _CSCMDTYPE
DESCRIPTOR.message_types_by_name['CSPlatformReservReq'] = _CSPLATFORMRESERVREQ
DESCRIPTOR.message_types_by_name['CSPlatformReservRes'] = _CSPLATFORMRESERVRES
DESCRIPTOR.enum_types_by_name['CSCMDType'] = _CSCMDTYPE

CSPlatformReservReq = _reflection.GeneratedProtocolMessageType('CSPlatformReservReq', (_message.Message,), dict(
  DESCRIPTOR = _CSPLATFORMRESERVREQ,
  __module__ = 'CSReserv_pb2'
  # @@protoc_insertion_point(class_scope:pb.platform.CSPlatformReservReq)
  ))
_sym_db.RegisterMessage(CSPlatformReservReq)

CSPlatformReservRes = _reflection.GeneratedProtocolMessageType('CSPlatformReservRes', (_message.Message,), dict(
  DESCRIPTOR = _CSPLATFORMRESERVRES,
  __module__ = 'CSReserv_pb2'
  # @@protoc_insertion_point(class_scope:pb.platform.CSPlatformReservRes)
  ))
_sym_db.RegisterMessage(CSPlatformReservRes)


# @@protoc_insertion_point(module_scope)
