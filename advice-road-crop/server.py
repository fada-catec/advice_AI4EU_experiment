import os
import grpc
from concurrent import futures
import time
from multiprocessing import cpu_count

from PIL import ImageFont, Image, ImageDraw
import io

import prepro_pb2
import prepro_pb2_grpc

import roadnet_test2 as roadnet

PORT = 8061

class ImagePreProcessServicer(prepro_pb2_grpc.ImagePreProcessServicer):

    def RoadCrop(self, request: prepro_pb2.Image, context):
        
        image_bytes = request.image_data
        img = Image.open(io.BytesIO(image_bytes)).convert('RGB')

        img_cropped = roadnet.roadnet(img)

        img_byte_arr = io.BytesIO()
        img_cropped.save(img_byte_arr, format='PNG')

        response = prepro_pb2.Image(image_data=img_byte_arr.getvalue())

        return response

# creat a grpc server :
server = grpc.server(futures.ThreadPoolExecutor(max_workers=cpu_count()-2))

prepro_pb2_grpc.add_ImagePreProcessServicer_to_server(ImagePreProcessServicer(), server)
print("Starting Server. Listening to port :" + str(PORT))
server.add_insecure_port("[::]:{}".format(PORT))
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)