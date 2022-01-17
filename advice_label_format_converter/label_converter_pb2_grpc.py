# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import label_converter_pb2 as label__converter__pb2


class LabelStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Convert = channel.unary_unary(
                '/Label/Convert',
                request_serializer=label__converter__pb2.OriginFormat.SerializeToString,
                response_deserializer=label__converter__pb2.Empty.FromString,
                )


class LabelServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Convert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LabelServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Convert': grpc.unary_unary_rpc_method_handler(
                    servicer.Convert,
                    request_deserializer=label__converter__pb2.OriginFormat.FromString,
                    response_serializer=label__converter__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Label', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Label(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Convert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Label/Convert',
            label__converter__pb2.OriginFormat.SerializeToString,
            label__converter__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)