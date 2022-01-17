# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: label.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='label.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0blabel.proto\"T\n\x0bObjDetected\x12\x0b\n\x03obj\x18\x01 \x01(\x05\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\x12\t\n\x01w\x18\x04 \x01(\x02\x12\t\n\x01h\x18\x05 \x01(\x02\x12\x0c\n\x04\x63onf\x18\x06 \x01(\x02\",\n\x0ePredictionData\x12\x1a\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x0c.ObjDetected\"\x07\n\x05\x45mpty2\'\n\x05Label\x12\x1e\n\x03Get\x12\x0f.PredictionData\x1a\x06.Emptyb\x06proto3'
)




_OBJDETECTED = _descriptor.Descriptor(
  name='ObjDetected',
  full_name='ObjDetected',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='obj', full_name='ObjDetected.obj', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='ObjDetected.x', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='ObjDetected.y', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='w', full_name='ObjDetected.w', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='h', full_name='ObjDetected.h', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='conf', full_name='ObjDetected.conf', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=15,
  serialized_end=99,
)


_PREDICTIONDATA = _descriptor.Descriptor(
  name='PredictionData',
  full_name='PredictionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='PredictionData.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=101,
  serialized_end=145,
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
  serialized_start=147,
  serialized_end=154,
)

_PREDICTIONDATA.fields_by_name['data'].message_type = _OBJDETECTED
DESCRIPTOR.message_types_by_name['ObjDetected'] = _OBJDETECTED
DESCRIPTOR.message_types_by_name['PredictionData'] = _PREDICTIONDATA
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjDetected = _reflection.GeneratedProtocolMessageType('ObjDetected', (_message.Message,), {
  'DESCRIPTOR' : _OBJDETECTED,
  '__module__' : 'label_pb2'
  # @@protoc_insertion_point(class_scope:ObjDetected)
  })
_sym_db.RegisterMessage(ObjDetected)

PredictionData = _reflection.GeneratedProtocolMessageType('PredictionData', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTIONDATA,
  '__module__' : 'label_pb2'
  # @@protoc_insertion_point(class_scope:PredictionData)
  })
_sym_db.RegisterMessage(PredictionData)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'label_pb2'
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
  serialized_start=156,
  serialized_end=195,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='Label.Get',
    index=0,
    containing_service=None,
    input_type=_PREDICTIONDATA,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LABEL)

DESCRIPTOR.services_by_name['Label'] = _LABEL

# @@protoc_insertion_point(module_scope)
