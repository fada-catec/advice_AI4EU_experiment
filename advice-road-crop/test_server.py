import grpc
from random import randint
from timeit import default_timer as timer

from PIL import ImageFont, Image, ImageDraw
import io

# import the generated classes
import prepro_pb2
import prepro_pb2_grpc
from google.protobuf import empty_pb2

start_ch = timer()
port_addr = 'localhost:8061'

# open a gRPC channel
channel = grpc.insecure_channel(port_addr)

# create a stub (client)
stub = prepro_pb2_grpc.ImagePreProcessStub(channel)
end_ch = timer()


request = prepro_pb2.Image()

with open('./imgs/test_img.jpg', 'rb') as fp:
    request.image_data = fp.read()

img_cropped = stub.RoadCrop(request)

img_cropped = Image.open(io.BytesIO(img_cropped.image_data)).convert('RGB')
img_cropped.show()
input()

# print('status of response:', grpc.StatusCode.OK.value)
# print('status of response:', grpc.StatusCode.name)
# for i in grpc.StatusCode:
#     print(i, i.value)