# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tendermint/store/types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tendermint/store/types.proto',
  package='tendermint.store',
  syntax='proto3',
  serialized_options=b'Z7github.com/tendermint/tendermint/proto/tendermint/store',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1ctendermint/store/types.proto\x12\x10tendermint.store\"/\n\x0f\x42lockStoreState\x12\x0c\n\x04\x62\x61se\x18\x01 \x01(\x03\x12\x0e\n\x06height\x18\x02 \x01(\x03\x42\x39Z7github.com/tendermint/tendermint/proto/tendermint/storeb\x06proto3'
)




_BLOCKSTORESTATE = _descriptor.Descriptor(
  name='BlockStoreState',
  full_name='tendermint.store.BlockStoreState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base', full_name='tendermint.store.BlockStoreState.base', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='tendermint.store.BlockStoreState.height', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=50,
  serialized_end=97,
)

DESCRIPTOR.message_types_by_name['BlockStoreState'] = _BLOCKSTORESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlockStoreState = _reflection.GeneratedProtocolMessageType('BlockStoreState', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKSTORESTATE,
  '__module__' : 'tendermint.store.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.store.BlockStoreState)
  })
_sym_db.RegisterMessage(BlockStoreState)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)