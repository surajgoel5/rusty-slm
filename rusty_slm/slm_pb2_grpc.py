# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import slm_pb2 as slm__pb2


class SLMStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetImage = channel.stream_unary(
                '/slm.SLM/SetImage',
                request_serializer=slm__pb2.ImageData.SerializeToString,
                response_deserializer=slm__pb2.Response.FromString,
                )
        self.SetScreen = channel.unary_unary(
                '/slm.SLM/SetScreen',
                request_serializer=slm__pb2.Screen.SerializeToString,
                response_deserializer=slm__pb2.Response.FromString,
                )
        self.SetPosition = channel.unary_unary(
                '/slm.SLM/SetPosition',
                request_serializer=slm__pb2.Position.SerializeToString,
                response_deserializer=slm__pb2.Response.FromString,
                )


class SLMServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetImage(self, request_iterator, context):
        """Set the image from a given image description and a stream of the image bytes
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetScreen(self, request, context):
        """Set the screen the slm is appearing on
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPosition(self, request, context):
        """Set the position on the screen
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SLMServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetImage': grpc.stream_unary_rpc_method_handler(
                    servicer.SetImage,
                    request_deserializer=slm__pb2.ImageData.FromString,
                    response_serializer=slm__pb2.Response.SerializeToString,
            ),
            'SetScreen': grpc.unary_unary_rpc_method_handler(
                    servicer.SetScreen,
                    request_deserializer=slm__pb2.Screen.FromString,
                    response_serializer=slm__pb2.Response.SerializeToString,
            ),
            'SetPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPosition,
                    request_deserializer=slm__pb2.Position.FromString,
                    response_serializer=slm__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'slm.SLM', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SLM(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetImage(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/slm.SLM/SetImage',
            slm__pb2.ImageData.SerializeToString,
            slm__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetScreen(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/slm.SLM/SetScreen',
            slm__pb2.Screen.SerializeToString,
            slm__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetPosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/slm.SLM/SetPosition',
            slm__pb2.Position.SerializeToString,
            slm__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)