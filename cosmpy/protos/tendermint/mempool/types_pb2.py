# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tendermint/mempool/types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tendermint/mempool/types.proto',
  package='tendermint.mempool',
  syntax='proto3',
  serialized_options=b'Z9github.com/tendermint/tendermint/proto/tendermint/mempool',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1etendermint/mempool/types.proto\x12\x12tendermint.mempool\"\x12\n\x03Txs\x12\x0b\n\x03txs\x18\x01 \x03(\x0c\"8\n\x07Message\x12&\n\x03txs\x18\x01 \x01(\x0b\x32\x17.tendermint.mempool.TxsH\x00\x42\x05\n\x03sumB;Z9github.com/tendermint/tendermint/proto/tendermint/mempoolb\x06proto3'
)




_TXS = _descriptor.Descriptor(
  name='Txs',
  full_name='tendermint.mempool.Txs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='txs', full_name='tendermint.mempool.Txs.txs', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=54,
  serialized_end=72,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='tendermint.mempool.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='txs', full_name='tendermint.mempool.Message.txs', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='sum', full_name='tendermint.mempool.Message.sum',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=74,
  serialized_end=130,
)

_MESSAGE.fields_by_name['txs'].message_type = _TXS
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['txs'])
_MESSAGE.fields_by_name['txs'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
DESCRIPTOR.message_types_by_name['Txs'] = _TXS
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Txs = _reflection.GeneratedProtocolMessageType('Txs', (_message.Message,), {
  'DESCRIPTOR' : _TXS,
  '__module__' : 'tendermint.mempool.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.mempool.Txs)
  })
_sym_db.RegisterMessage(Txs)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'tendermint.mempool.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.mempool.Message)
  })
_sym_db.RegisterMessage(Message)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)