import grpc
from random import randint
from timeit import default_timer as timer

from PIL import ImageFont, Image, ImageDraw
import os
from tqdm import tqdm

# import the generated classes
import yolo_pb2
import yolo_pb2_grpc

start_ch = timer()
port_addr = 'localhost:8061'

# open a gRPC channel
channel = grpc.insecure_channel(port_addr)

# create a stub (client)
stub = yolo_pb2_grpc.YOLOStub(channel)
end_ch = timer()

request = yolo_pb2.Image()

labels_path = os.path.join(os.getcwd(), 'imgs')
predictions_path = os.path.join(os.getcwd(), 'pred_labels')

img_names = os.listdir(labels_path)

for x in tqdm(img_names):

    with open(os.path.join(labels_path, x), 'rb') as fp:
        request.image_data = fp.read()

    prediction = stub.Detect(request)

    if (len(prediction.data) == 0):
        yolo_str = ''
    else:
        for data in prediction.data:
            yolo_str = str(data.obj)+' '+str(data.x)+' '+str(data.y)+' '+str(data.w)+' '+str(data.h)+' '+str(data.conf)+'\n'

    with open(os.path.join(predictions_path, x.replace('jpg','txt')), 'a+') as f:
        f.write(yolo_str)


# print(prediction)
# input()