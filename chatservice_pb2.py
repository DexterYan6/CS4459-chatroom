# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: chatservice.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'chatservice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63hatservice.proto\"3\n\x0eMessageRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"4\n\x0fMessageResponse\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2k\n\x0b\x43hatService\x12\x32\n\x0bSendMessage\x12\x0f.MessageRequest\x1a\x10.MessageResponse\"\x00\x12(\n\nChatStream\x12\x06.Empty\x1a\x10.MessageResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chatservice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MESSAGEREQUEST']._serialized_start=21
  _globals['_MESSAGEREQUEST']._serialized_end=72
  _globals['_MESSAGERESPONSE']._serialized_start=74
  _globals['_MESSAGERESPONSE']._serialized_end=126
  _globals['_EMPTY']._serialized_start=128
  _globals['_EMPTY']._serialized_end=135
  _globals['_CHATSERVICE']._serialized_start=137
  _globals['_CHATSERVICE']._serialized_end=244
# @@protoc_insertion_point(module_scope)
