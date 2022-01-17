import os
from shutil import copy
import grpc
from concurrent import futures
import time
from multiprocessing import cpu_count

import databroker_pb2
import databroker_pb2_grpc

from shutil import copy, copytree, rmtree

PORT = 8061

shared_folder = os.getenv("SHARED_FOLDER_PATH")

i = 0
imgspath = [os.path.join(shared_folder+'/img', x) for x in os.listdir(shared_folder+'/img') if x[-3:] == "jpg"]
imgspath = sorted(imgspath)

class ImageSourceServicer(databroker_pb2_grpc.ImageSourceServicer):

    def Get(self, request, context):

        global i, imgspath

        if i<len(imgspath):

            with open(imgspath[i], 'rb') as fp:
                image_bytes = fp.read()

            response = databroker_pb2.Image(image_data=image_bytes)

            i+=1

            return response
        else:
            print("No more images")

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