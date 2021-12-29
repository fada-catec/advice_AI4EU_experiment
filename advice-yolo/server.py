import grpc
from concurrent import futures
import time
from multiprocessing import cpu_count
import numpy as np

from PIL import Image
import cv2
import io

import yolo_pb2
import yolo_pb2_grpc

import detection

PORT = 8002

class YOLOServicer(yolo_pb2_grpc.YOLOServicer):

    def Detect(self, request: yolo_pb2.Image, context):

        no_crop_img_height = 720
        
        image_bytes = request.image_data
        img = Image.open(io.BytesIO(image_bytes)).convert('RGB')

        imgcv = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)

        detection_data = detection.main(imgcv, no_crop_img_height)

        data = yolo_pb2.PredictionData()

        for i in range(len(detection_data)):

            data_obj = yolo_pb2.ObjDetected()

            data_obj.obj = detection_data[i][0]
            data_obj.x = detection_data[i][1]
            data_obj.y = detection_data[i][2]
            data_obj.w = detection_data[i][3]
            data_obj.h = detection_data[i][4]
            data_obj.conf = detection_data[i][5]

            data.data.append(data_obj)

        response = data

        return response

# create a grpc server :
server = grpc.server(futures.ThreadPoolExecutor(max_workers=cpu_count()-2))

yolo_pb2_grpc.add_YOLOServicer_to_server(YOLOServicer(), server)
print("Starting Server. Listening to port :" + str(PORT))
server.add_insecure_port("[::]:{}".format(PORT))
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)