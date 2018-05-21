# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

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
  name='test.proto',
  package='test',
  syntax='proto3',
  serialized_pb=_b('\n\ntest.proto\x12\x04test\"2\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\x18\n\nGetPayload\x12\n\n\x02id\x18\x01 \x01(\x03\"\x07\n\x05\x45mpty2^\n\x0bTestService\x12\'\n\x07GetUser\x12\x10.test.GetPayload\x1a\n.test.User\x12&\n\tListUsers\x12\x0b.test.Empty\x1a\n.test.User0\x01\x62\x06proto3')
)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='test.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='test.User.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='test.User.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='test.User.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=70,
)


_GETPAYLOAD = _descriptor.Descriptor(
  name='GetPayload',
  full_name='test.GetPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='test.GetPayload.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=96,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='test.Empty',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=105,
)

DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['GetPayload'] = _GETPAYLOAD
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.User)
  ))
_sym_db.RegisterMessage(User)

GetPayload = _reflection.GeneratedProtocolMessageType('GetPayload', (_message.Message,), dict(
  DESCRIPTOR = _GETPAYLOAD,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.GetPayload)
  ))
_sym_db.RegisterMessage(GetPayload)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.Empty)
  ))
_sym_db.RegisterMessage(Empty)



_TESTSERVICE = _descriptor.ServiceDescriptor(
  name='TestService',
  full_name='test.TestService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=107,
  serialized_end=201,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUser',
    full_name='test.TestService.GetUser',
    index=0,
    containing_service=None,
    input_type=_GETPAYLOAD,
    output_type=_USER,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListUsers',
    full_name='test.TestService.ListUsers',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_USER,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name['TestService'] = _TESTSERVICE

# @@protoc_insertion_point(module_scope)
