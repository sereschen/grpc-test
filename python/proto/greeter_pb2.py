# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: greeter.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 6, 31, 0, "", "greeter.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\rgreeter.proto\x12\x07greeter"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2C\n\x07Greeter\x12\x38\n\x08SayHello\x12\x15.greeter.HelloRequest\x1a\x13.greeter.HelloReply"\x00\x42\x0bZ\t.;greeterb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "greeter_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z\t.;greeter"
    _globals["_HELLOREQUEST"]._serialized_start = 26
    _globals["_HELLOREQUEST"]._serialized_end = 54
    _globals["_HELLOREPLY"]._serialized_start = 56
    _globals["_HELLOREPLY"]._serialized_end = 85
    _globals["_GREETER"]._serialized_start = 87
    _globals["_GREETER"]._serialized_end = 154
# @@protoc_insertion_point(module_scope)
