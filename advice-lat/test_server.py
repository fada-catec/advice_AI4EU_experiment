import grpc
from random import randint
from timeit import default_timer as timer
import os
from tqdm import tqdm

# import the generated classes
import label_pb2
import label_pb2_grpc

start_ch = timer()
port_addr = 'localhost:8003'

# open a gRPC channel
channel = grpc.insecure_channel(port_addr)

# create a stub (client)
stub = label_pb2_grpc.LabelStub(channel)
end_ch = timer()

shared_folder = os.path.join('/home/arodriguez/advice-local-pipeline/shared_folder')

labels_path = os.path.join(shared_folder, 'pred_labels')

labelspath = [os.path.join(labels_path, x) for x in os.listdir(labels_path) if x[-3:] == "txt"]

for l_path in tqdm(labelspath):
    request = label_pb2.PredictionData()
    detection_data = []

    with open(l_path, 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            detection_data_line = line.split(' ')
            detection_data.append(detection_data_line)

    for i in range(len(detection_data)):

        data_obj = label_pb2.ObjDetected()

        data_obj.obj = int(detection_data[i][0])
        data_obj.x = float(detection_data[i][1])
        data_obj.y = float(detection_data[i][2])
        data_obj.w = float(detection_data[i][3])
        data_obj.h = float(detection_data[i][4])
        data_obj.conf = float(detection_data[i][5])

        request.data.append(data_obj)

    # print(request)

    prediction = stub.Get(request)

    # print(prediction)
    # input()