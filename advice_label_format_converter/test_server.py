import grpc
from random import randint
from timeit import default_timer as timer

# import the generated classes
import label_converter_pb2
import label_converter_pb2_grpc

start_ch = timer()
port_addr = 'localhost:8061'

# open a gRPC channel
channel = grpc.insecure_channel(port_addr)

# create a stub (client)
stub = label_converter_pb2_grpc.LabelStub(channel)
end_ch = timer()

request = label_converter_pb2.OriginFormat()

request.format = "PASCAL"

conversion = stub.Convert(request)

print(conversion)