import os
import grpc
from concurrent import futures
import time
from multiprocessing import cpu_count

import databroker_pb2
import databroker_pb2_grpc

PORT = 8061

class ImageSourceServicer(databroker_pb2_grpc.ImageSourceServicer):

    def Get(self, request, context):

        image_path = os.getcwd() + 'imgs/test_img.jpg'

        with open(image_path, 'rb') as fp:
            image_bytes = fp.read()

        response = databroker_pb2.Image(image_data=image_bytes)

        return response

# creat a grpc server :
server = grpc.server(futures.ThreadPoolExecutor(max_workers=cpu_count()-2))

databroker_pb2_grpc.add_ImageSourceServicer_to_server(ImageSourceServicer(), server)
print("Starting Server. Listening to port :" + str(PORT))
server.add_insecure_port("[::]:{}".format(PORT))
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)