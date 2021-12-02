import grpc
from concurrent import futures
import time
from multiprocessing import cpu_count

import os
from shutil import copy, rmtree
from shutil import copytree


import label_converter_pb2
import label_converter_pb2_grpc

import label_converter

PORT = 8061
shared_folder = os.getenv("SHARED_FOLDER_PATH")
# shared_folder = os.path.join(os.getcwd(), 'shared_folder') #for debug

label_path = os.path.join(os.getcwd(), 'labels')
classes_path = os.path.join(os.getcwd(), 'classes.json')

if os.path.isdir(shared_folder+'/labels'):
    rmtree(shared_folder+'/labels')

copytree(label_path, shared_folder+'/labels')
copy(classes_path, shared_folder)

class LabelServicer(label_converter_pb2_grpc.LabelServicer):
        def Convert(self, request: label_converter_pb2.OriginFormat, context):
            origin_format = request.format

            label_converter.main(origin_format)

            empty_msg = label_converter_pb2.Empty()
            
            return empty_msg

server = grpc.server(futures.ThreadPoolExecutor(max_workers=cpu_count()-2))

label_converter_pb2_grpc.add_LabelServicer_to_server(LabelServicer(), server)
print("Starting Server. Listening to port :" + str(PORT))
server.add_insecure_port("[::]:{}".format(PORT))
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)