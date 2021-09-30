import grpc
from random import randint
from timeit import default_timer as timer

from PIL import ImageFont, Image, ImageDraw
import io

# import the generated classes
import databroker_pb2
import databroker_pb2_grpc
from google.protobuf import empty_pb2

start_ch = timer()
port_addr = 'localhost:8061'

# open a gRPC channel
channel = grpc.insecure_channel(port_addr)

# create a stub (client)
stub = databroker_pb2_grpc.ImageSourceStub(channel)
end_ch = timer()

request = empty_pb2.Empty()
img = stub.Get(request)
img = Image.open(io.BytesIO(img.image_data)).convert('RGB')
img.show()
input()

# print('status of response:', grpc.StatusCode.OK.value)
# print('status of response:', grpc.StatusCode.name)
# for i in grpc.StatusCode:
#     print(i, i.value)