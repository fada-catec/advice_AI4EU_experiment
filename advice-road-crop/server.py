import os
import grpc
from concurrent import futures
import time
from multiprocessing import cpu_count

import tensorflow as tf
from PIL import ImageFont, Image, ImageDraw
import io

import prepro_pb2
import prepro_pb2_grpc

import roadnet_test

PORT = 8001

class ImagePreProcessServicer(prepro_pb2_grpc.ImagePreProcessServicer):
    
    def __init__(self):
        self.session = tf.Session()
        self.graph = tf.get_default_graph()

        with self.graph.as_default():
            with self.session.as_default():
                # When you create a Model, the session hasn't been restored yet. 
                # All placeholders, variables and ops that are defined in Model.__init__ are placed in a new graph, 
                # which makes itself a default graph inside with block
                self.roadnet_model = roadnet_test.RoadNetModel()

    def RoadCrop(self, request, context):
        
        image_bytes = request.image_data
        img = Image.open(io.BytesIO(image_bytes)).convert('RGB')

        with self.graph.as_default():
            with self.session.as_default():
                img_cropped = self.roadnet_model.predict(img)

        img_byte_arr = io.BytesIO()
        img_cropped.save(img_byte_arr, format='PNG')

        response = prepro_pb2.Image(image_data=img_byte_arr.getvalue())

        return response


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