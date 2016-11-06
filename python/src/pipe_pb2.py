# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pipe.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pipe.proto',
  package='',
  serialized_pb=_b('\n\npipe.proto\x1a\x0c\x63ommon.proto\"\xc4\x01\n\x08\x46ileTask\x12\x10\n\x08\x63hunk_no\x18\x01 \x01(\x05\x12\r\n\x05\x63hunk\x18\x02 \x01(\x0c\x12\x10\n\x08\x66ilename\x18\x03 \x02(\t\x12.\n\x0e\x66ile_task_type\x18\x04 \x02(\x0e\x32\x16.FileTask.FileTaskType\x12\x14\n\x0c\x63hunk_counts\x18\x05 \x01(\x05\x12\x0e\n\x06sender\x18\x06 \x02(\t\"/\n\x0c\x46ileTaskType\x12\x08\n\x04READ\x10\x01\x12\t\n\x05WRITE\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\"\x9d\x01\n\x0e\x43ommandMessage\x12\x17\n\x06header\x18\x01 \x02(\x0b\x32\x07.Header\x12\x1b\n\x08\x66iletask\x18\x02 \x01(\x0b\x32\t.FileTask\x12\x0e\n\x04\x66ile\x18\x06 \x01(\x0cH\x00\x12\x0e\n\x04ping\x18\x03 \x01(\x08H\x00\x12\x11\n\x07message\x18\x04 \x01(\tH\x00\x12\x17\n\x03\x65rr\x18\x05 \x01(\x0b\x32\x08.FailureH\x00\x42\t\n\x07payloadB\x0b\n\x07routingH\x01')
  ,
  dependencies=[common_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_FILETASK_FILETASKTYPE = _descriptor.EnumDescriptor(
  name='FileTaskType',
  full_name='FileTask.FileTaskType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READ', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRITE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=178,
  serialized_end=225,
)
_sym_db.RegisterEnumDescriptor(_FILETASK_FILETASKTYPE)


_FILETASK = _descriptor.Descriptor(
  name='FileTask',
  full_name='FileTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk_no', full_name='FileTask.chunk_no', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chunk', full_name='FileTask.chunk', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filename', full_name='FileTask.filename', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_task_type', full_name='FileTask.file_task_type', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chunk_counts', full_name='FileTask.chunk_counts', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender', full_name='FileTask.sender', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FILETASK_FILETASKTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=225,
)


_COMMANDMESSAGE = _descriptor.Descriptor(
  name='CommandMessage',
  full_name='CommandMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='CommandMessage.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filetask', full_name='CommandMessage.filetask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file', full_name='CommandMessage.file', index=2,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ping', full_name='CommandMessage.ping', index=3,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='CommandMessage.message', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err', full_name='CommandMessage.err', index=5,
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='CommandMessage.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=228,
  serialized_end=385,
)

_FILETASK.fields_by_name['file_task_type'].enum_type = _FILETASK_FILETASKTYPE
_FILETASK_FILETASKTYPE.containing_type = _FILETASK
_COMMANDMESSAGE.fields_by_name['header'].message_type = common_pb2._HEADER
_COMMANDMESSAGE.fields_by_name['filetask'].message_type = _FILETASK
_COMMANDMESSAGE.fields_by_name['err'].message_type = common_pb2._FAILURE
_COMMANDMESSAGE.oneofs_by_name['payload'].fields.append(
  _COMMANDMESSAGE.fields_by_name['file'])
_COMMANDMESSAGE.fields_by_name['file'].containing_oneof = _COMMANDMESSAGE.oneofs_by_name['payload']
_COMMANDMESSAGE.oneofs_by_name['payload'].fields.append(
  _COMMANDMESSAGE.fields_by_name['ping'])
_COMMANDMESSAGE.fields_by_name['ping'].containing_oneof = _COMMANDMESSAGE.oneofs_by_name['payload']
_COMMANDMESSAGE.oneofs_by_name['payload'].fields.append(
  _COMMANDMESSAGE.fields_by_name['message'])
_COMMANDMESSAGE.fields_by_name['message'].containing_oneof = _COMMANDMESSAGE.oneofs_by_name['payload']
_COMMANDMESSAGE.oneofs_by_name['payload'].fields.append(
  _COMMANDMESSAGE.fields_by_name['err'])
_COMMANDMESSAGE.fields_by_name['err'].containing_oneof = _COMMANDMESSAGE.oneofs_by_name['payload']
DESCRIPTOR.message_types_by_name['FileTask'] = _FILETASK
DESCRIPTOR.message_types_by_name['CommandMessage'] = _COMMANDMESSAGE

FileTask = _reflection.GeneratedProtocolMessageType('FileTask', (_message.Message,), dict(
  DESCRIPTOR = _FILETASK,
  __module__ = 'pipe_pb2'
  # @@protoc_insertion_point(class_scope:FileTask)
  ))
_sym_db.RegisterMessage(FileTask)

CommandMessage = _reflection.GeneratedProtocolMessageType('CommandMessage', (_message.Message,), dict(
  DESCRIPTOR = _COMMANDMESSAGE,
  __module__ = 'pipe_pb2'
  # @@protoc_insertion_point(class_scope:CommandMessage)
  ))
_sym_db.RegisterMessage(CommandMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\007routingH\001'))
# @@protoc_insertion_point(module_scope)
