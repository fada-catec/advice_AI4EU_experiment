# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: label_converter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='label_converter.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15label_converter.proto\"\x1e\n\x0cOriginFormat\x12\x0e\n\x06\x66ormat\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2)\n\x05Label\x12 \n\x07\x43onvert\x12\r.OriginFormat\x1a\x06.Emptyb\x06proto3'
)




_ORIGINFORMAT = _descriptor.Descriptor(
  name='OriginFormat',
  full_name='OriginFormat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='format', full_name='OriginFormat.format', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=55,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=64,
)

DESCRIPTOR.message_types_by_name['OriginFormat'] = _ORIGINFORMAT
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OriginFormat = _reflection.GeneratedProtocolMessageType('OriginFormat', (_message.Message,), {
  'DESCRIPTOR' : _ORIGINFORMAT,
  '__module__' : 'label_converter_pb2'
  # @@protoc_insertion_point(class_scope:OriginFormat)
  })
_sym_db.RegisterMessage(OriginFormat)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'label_converter_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)



_LABEL = _descriptor.ServiceDescriptor(
  name='Label',
  full_name='Label',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=66,
  serialized_end=107,
  methods=[
  _descriptor.MethodDescriptor(
    name='Convert',
    full_name='Label.Convert',
    index=0,
    containing_service=None,
    input_type=_ORIGINFORMAT,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LABEL)

DESCRIPTOR.services_by_name['Label'] = _LABEL

# @@protoc_insertion_point(module_scope)
