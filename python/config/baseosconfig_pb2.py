# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config/baseosconfig.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from config import devcommon_pb2 as config_dot_devcommon__pb2
from config import storage_pb2 as config_dot_storage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63onfig/baseosconfig.proto\x12\x15org.lfedge.eve.config\x1a\x16\x63onfig/devcommon.proto\x1a\x14\x63onfig/storage.proto\"\x0b\n\tOSKeyTags\"\x0e\n\x0cOSVerDetails\"\xb6\x01\n\x0c\x42\x61seOSConfig\x12=\n\x0euuidandversion\x18\x01 \x01(\x0b\x32%.org.lfedge.eve.config.UUIDandVersion\x12,\n\x06\x64rives\x18\x03 \x03(\x0b\x32\x1c.org.lfedge.eve.config.Drive\x12\x10\n\x08\x61\x63tivate\x18\x04 \x01(\x08\x12\x15\n\rbaseOSVersion\x18\n \x01(\t\x12\x10\n\x08volumeID\x18\x0c \x01(\t\"\x89\x01\n\x06\x42\x61seOS\x12\x19\n\x11\x63ontent_tree_uuid\x18\x01 \x01(\t\x12\x39\n\x0cretry_update\x18\x02 \x01(\x0b\x32#.org.lfedge.eve.config.DeviceOpsCmd\x12\x10\n\x08\x61\x63tivate\x18\x03 \x01(\x08\x12\x17\n\x0f\x62\x61se_os_version\x18\x04 \x01(\tB=\n\x15org.lfedge.eve.configZ$github.com/lf-edge/eve-api/go/configb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'config.baseosconfig_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025org.lfedge.eve.configZ$github.com/lf-edge/eve-api/go/config'
  _OSKEYTAGS._serialized_start=98
  _OSKEYTAGS._serialized_end=109
  _OSVERDETAILS._serialized_start=111
  _OSVERDETAILS._serialized_end=125
  _BASEOSCONFIG._serialized_start=128
  _BASEOSCONFIG._serialized_end=310
  _BASEOS._serialized_start=313
  _BASEOS._serialized_end=450
# @@protoc_insertion_point(module_scope)
