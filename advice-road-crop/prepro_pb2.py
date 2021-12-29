# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prepro.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='prepro.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cprepro.proto\"\x1b\n\x05Image\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\x32-\n\x0fImagePreProcess\x12\x1a\n\x08RoadCrop\x12\x06.Image\x1a\x06.Imageb\x06proto3'
)




_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_data', full_name='Image.image_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=16,
  serialized_end=43,
)

DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'prepro_pb2'
  # @@protoc_insertion_point(class_scope:Image)
  })
_sym_db.RegisterMessage(Image)



_IMAGEPREPROCESS = _descriptor.ServiceDescriptor(
  name='ImagePreProcess',
  full_name='ImagePreProcess',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=45,
  serialized_end=90,
  methods=[
  _descriptor.MethodDescriptor(
    name='RoadCrop',
    full_name='ImagePreProcess.RoadCrop',
    index=0,
    containing_service=None,
    input_type=_IMAGE,
    output_type=_IMAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGEPREPROCESS)

DESCRIPTOR.services_by_name['ImagePreProcess'] = _IMAGEPREPROCESS

# @@protoc_insertion_point(module_scope)
