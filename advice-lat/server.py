from typing import Optional, List
import os
import logging
import json
import fastapi
import fastapi.templating
# import pydantic
import grpc
from concurrent import futures
from multiprocessing import cpu_count
import base64
import cv2
import queue

import label_pb2
import label_pb2_grpc

index = 0
logger  = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = fastapi.FastAPI(title='LabelingServer', debug=True)
app.logger = logger
templates = fastapi.templating.Jinja2Templates(directory='templates')

PORT = 8061

protobuf_to_js_queue = queue.Queue()

class LabelServicer(label_pb2_grpc.LabelServicer):
    def Get(self, request: label_pb2.PredictionData, context):

        global detection_data_put

        detection_data_put = request.data

        protobuf_to_js_queue.put(detection_data_put)

        empty_msg = label_pb2.Empty()
        return empty_msg


# create a grpc server :
server = grpc.server(futures.ThreadPoolExecutor(max_workers=cpu_count()-2))

label_pb2_grpc.add_LabelServicer_to_server(LabelServicer(), server)
print("Starting Server. Listening to port :" + str(PORT))
server.add_insecure_port("[::]:{}".format(PORT))
server.start()

def getClasses(file_name):
    path = os.path.join(os.getcwd(), file_name)

    with open(path) as f:
        classes = json.load(f)

    return classes

@app.get('/')
def serve_website(request: fastapi.Request):
    global index
    index = 0
    return templates.TemplateResponse("gui.html", { 'request': request }, headers={'Cache-Control': 'no-cache'})

@app.get('/tool.html')
def serve_website(request: fastapi.Request):
    global index
    index = 0
    return templates.TemplateResponse("tool.html", { 'request': request }, headers={'Cache-Control': 'no-cache'})

@app.get('/contact.html')
def serve_website(request: fastapi.Request):

    global index
    index = 0
    return templates.TemplateResponse("contact.html", { 'request': request }, headers={'Cache-Control': 'no-cache'})

@app.get('/gui.js')
def serve_js(request: fastapi.Request):
    return fastapi.responses.FileResponse("gui.js", headers={'Cache-Control': 'no-cache'})

@app.get('/gui.css')
def serve_css(request: fastapi.Request):
   return fastapi.responses.FileResponse("gui.css", headers={'Cache-Control': 'no-cache'})

@app.put('/save_result', response_model=None)
def save_result(filename:str, result: str) -> None:

    print(protobuf_to_js_queue.qsize()) #debug porpuse

    classes_dict = getClasses(os.path.join(os.getcwd(), "shared_folder", "classes.json"))
    result = result.split(',')
    save_path = os.path.join(os.getcwd(), "shared_folder", "new_labels", filename)
    label_string=''

    if result[0] != '':
        for i in range(0, len(result), 5):
            label = result[i:i+5]
            for j in range(len(label)-1):
                label[j+1] = float(label[j+1])

            label[1] = (label[1] + (label[3]/2))/img_shape[1]
            label[2] = (label[2] + (label[4]/2))/img_shape[0]
            label[3] = label[3]/img_shape[1]
            label[4] = label[4]/img_shape[0]

            label_string = label_string + str(classes_dict[label[0]]) +' '+str(label[1])+' '+str(label[2])+' '+str(label[3])+' '+str(label[4])+'\n'

    with open(save_path, 'w') as f:
        f.write(label_string)

    print('\nSaved "'+filename+'" with labels: ')

    print(label_string)

    return None

def update_filename():

    global index

    labels_path = os.path.join(os.getcwd(), 'shared_folder', 'orig_labels')
    img_path = os.path.join(os.getcwd(), 'shared_folder', 'img')

    labelspath = [os.path.join(labels_path, x) for x in os.listdir(labels_path) if x[-3:] == "txt"]

    if index <= len(labelspath)-1:

        imgpath = os.path.join(img_path, labelspath[index].split('/')[-1].replace('txt','jpg'))

    else:
        index-=1
        imgpath = os.path.join(img_path, labelspath[index].split('/')[-1].replace('txt','jpg'))

        print("No more images")

        index = 0

        return False

    return labelspath[index], imgpath, len(labelspath)

@app.get('/request')
def request(request: fastapi.Request):

    ret = []
    global index

    filespath = update_filename()
    if filespath != False:

        print(filespath)
        index+=1

        #Get needed parameters
        classes_dict = getClasses(os.path.join(os.getcwd(), "shared_folder", "classes.json"))
        global img_shape

        #Get image
        image_path = filespath[1]

        img = cv2.imread(image_path)
        img_shape = img.shape
        _, im_arr = cv2.imencode('.jpg', img)
        im_bytes = im_arr.tobytes()
        image_base64=base64.b64encode(im_bytes)

        ret3 = image_base64

        #Get original labels
        label_path = filespath[0]
        actual_image = label_path.split('/')[-1]
        ret2 = []

        with open(label_path, 'rb') as fp:
            labels_coded = fp.readlines()

        keys = list(classes_dict.keys())
        for x in labels_coded:
            labels_decoded = [ float(i) for i in x.decode().split()]

            labels_decoded[0] = keys[int(labels_decoded[0])]
            labels_decoded[1] = round((labels_decoded[1]-(labels_decoded[3]/2))*img_shape[1], 2) # [cx_yolo - (w_yolo/2)] * w_imagen
            labels_decoded[2] = round((labels_decoded[2]-(labels_decoded[4]/2))*img_shape[0], 2) # [cy_yolo - (y_yolo/2)] * y_imagen
            labels_decoded[3] = round(labels_decoded[3]*img_shape[1], 2) # w_yolo * w_imagen
            labels_decoded[4] = round(labels_decoded[4]*img_shape[0], 2) # h_yolo * h_imagen
            
            ret2.append(labels_decoded)

        #Get predicted labels
        detection_data_get = protobuf_to_js_queue.get()

        for i in detection_data_get:
            defect = [keys[i.obj], round(i.x*img_shape[1],2), round(i.y*img_shape[0],2), round(i.w*img_shape[1],2), round(i.h*img_shape[0],2), round(i.conf,2)]
            ret.append(defect)

        return ret, ret2, ret3, actual_image, index, filespath[2]
    else:
        return False