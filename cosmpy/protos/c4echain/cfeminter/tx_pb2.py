# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: c4echain/cfeminter/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from c4echain.cfeminter import params_pb2 as c4echain_dot_cfeminter_dot_params__pb2
from c4echain.cfeminter import minter_pb2 as c4echain_dot_cfeminter_dot_minter__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x63\x34\x65\x63hain/cfeminter/tx.proto\x12\x1f\x63hain4energy.c4echain.cfeminter\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1f\x63\x34\x65\x63hain/cfeminter/params.proto\x1a\x1f\x63\x34\x65\x63hain/cfeminter/minter.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xac\x01\n\x0fMsgUpdateParams\x12\x11\n\tauthority\x18\x01 \x01(\t\x12\x12\n\nmint_denom\x18\x02 \x01(\t\x12\x38\n\nstart_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x38\n\x07minters\x18\x04 \x03(\x0b\x32\'.chain4energy.c4echain.cfeminter.Minter\"\x19\n\x17MsgUpdateParamsResponse\"\x9f\x01\n\x16MsgUpdateMintersParams\x12\x11\n\tauthority\x18\x01 \x01(\t\x12\x38\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x38\n\x07minters\x18\x03 \x03(\x0b\x32\'.chain4energy.c4echain.cfeminter.Minter\" \n\x1eMsgUpdateMintersParamsResponse2\x93\x02\n\x03Msg\x12\x8f\x01\n\x13UpdateMintersParams\x12\x37.chain4energy.c4echain.cfeminter.MsgUpdateMintersParams\x1a?.chain4energy.c4echain.cfeminter.MsgUpdateMintersParamsResponse\x12z\n\x0cUpdateParams\x12\x30.chain4energy.c4echain.cfeminter.MsgUpdateParams\x1a\x38.chain4energy.c4echain.cfeminter.MsgUpdateParamsResponseB5Z3github.com/chain4energy/c4e-chain/x/cfeminter/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'c4echain.cfeminter.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z3github.com/chain4energy/c4e-chain/x/cfeminter/types'
  _MSGUPDATEPARAMS.fields_by_name['start_time']._options = None
  _MSGUPDATEPARAMS.fields_by_name['start_time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _MSGUPDATEMINTERSPARAMS.fields_by_name['start_time']._options = None
  _MSGUPDATEMINTERSPARAMS.fields_by_name['start_time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _MSGUPDATEPARAMS._serialized_start=238
  _MSGUPDATEPARAMS._serialized_end=410
  _MSGUPDATEPARAMSRESPONSE._serialized_start=412
  _MSGUPDATEPARAMSRESPONSE._serialized_end=437
  _MSGUPDATEMINTERSPARAMS._serialized_start=440
  _MSGUPDATEMINTERSPARAMS._serialized_end=599
  _MSGUPDATEMINTERSPARAMSRESPONSE._serialized_start=601
  _MSGUPDATEMINTERSPARAMSRESPONSE._serialized_end=633
  _MSG._serialized_start=636
  _MSG._serialized_end=911
# @@protoc_insertion_point(module_scope)