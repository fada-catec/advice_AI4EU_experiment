# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import orchestrator_pb2 as orchestrator__pb2


class ImageSourceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/ImageSource/Get',
                request_serializer=orchestrator__pb2.Empty.SerializeToString,
                response_deserializer=orchestrator__pb2.Image.FromString,
                )


class ImageSourceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageSourceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=orchestrator__pb2.Empty.FromString,
                    response_serializer=orchestrator__pb2.Image.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ImageSource', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageSource(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ImageSource/Get',
            orchestrator__pb2.Empty.SerializeToString,
            orchestrator__pb2.Image.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ImagePreProcessStub(object):
    """Additional ROI

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RoadCrop = channel.unary_unary(
                '/ImagePreProcess/RoadCrop',
                request_serializer=orchestrator__pb2.Image.SerializeToString,
                response_deserializer=orchestrator__pb2.Image.FromString,
                )


class ImagePreProcessServicer(object):
    """Additional ROI

    """

    def RoadCrop(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImagePreProcessServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RoadCrop': grpc.unary_unary_rpc_method_handler(
                    servicer.RoadCrop,
                    request_deserializer=orchestrator__pb2.Image.FromString,
                    response_serializer=orchestrator__pb2.Image.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ImagePreProcess', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImagePreProcess(object):
    """Additional ROI

    """

    @staticmethod
    def RoadCrop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ImagePreProcess/RoadCrop',
            orchestrator__pb2.Image.SerializeToString,
            orchestrator__pb2.Image.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class YOLOStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Detect = channel.unary_unary(
                '/YOLO/Detect',
                request_serializer=orchestrator__pb2.Image.SerializeToString,
                response_deserializer=orchestrator__pb2.PredictionData.FromString,
                )


class YOLOServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Detect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_YOLOServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Detect': grpc.unary_unary_rpc_method_handler(
                    servicer.Detect,
                    request_deserializer=orchestrator__pb2.Image.FromString,
                    response_serializer=orchestrator__pb2.PredictionData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'YOLO', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class YOLO(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Detect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YOLO/Detect',
            orchestrator__pb2.Image.SerializeToString,
            orchestrator__pb2.PredictionData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class LabelStub(object):
    """Additional LAT

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/Label/Get',
                request_serializer=orchestrator__pb2.PredictionData.SerializeToString,
                response_deserializer=orchestrator__pb2.Empty.FromString,
                )


class LabelServicer(object):
    """Additional LAT

    """

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LabelServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=orchestrator__pb2.PredictionData.FromString,
                    response_serializer=orchestrator__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Label', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Label(object):
    """Additional LAT

    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Label/Get',
            orchestrator__pb2.PredictionData.SerializeToString,
            orchestrator__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
