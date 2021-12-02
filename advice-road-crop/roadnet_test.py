import os
from shutil import rmtree

import cv2
import json
import keras
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image
from PIL import ImageFont, Image, ImageDraw
import io

import segmentation_models as sm

from roadnet.utils import visualize, denormalize
from roadnet.data_aug import get_preprocessing
from roadnet.net import roadnet_rt

import convert_voc_to_yolo_crop as yolo_crop


# in_dir = '/home/catec/rluque_ws/RoadNet-RT-main/dataset/train5_valid_15percent_imgs' #images only
# xml_dir = '/home/catec/rluque_ws/RoadNet-RT-main/dataset/train5_valid_15percent_xml' #xml only
# out_dir = '/home/catec/rluque_ws/RoadNet-RT-main/dataset/train5_valid_15percent_out' #output dir


class RoadNetModel():
    
    def __init__(self):

        print("init")
        config_path = "./roadnet/config.json"
        with open(config_path) as config_buffer:
            config = json.loads(config_buffer.read())

        # BACKBONE = config["model"]["BACKBONE"]
        CLASSES = config["model"]["CLASSES"].split("delimiter")
        # BATCH_SIZE = config["train"]["BATCH_SIZE"]
        LR = config["train"]["LR"]
        # EPOCHS = config["train"]["EPOCHS"]
        self.HEIGHT = 280 #352 # HEIGHT = config["model"]["IN_HEIGHT"]
        self.WIDTH = 960 #1216 # WIDTH = config["model"]["IN_WIDTH"]

        n_classes = 1 if len(CLASSES) == 1 else (len(CLASSES) + 1)  # case for binary and multiclass segmentation
        activation = 'sigmoid' if n_classes == 1 else 'softmax'
        
        self.model = roadnet_rt((self.HEIGHT, self.WIDTH), n_classes, activation).build()
        # model.summary()
        self.model.load_weights('./roadnet_rt_9257.hdf5')

        optim = keras.optimizers.Adam(LR)
        dice_loss = sm.losses.DiceLoss()
        focal_loss = sm.losses.BinaryFocalLoss() if n_classes == 1 else sm.losses.CategoricalFocalLoss()
        total_loss = dice_loss + (1 * focal_loss)

        metrics = [sm.metrics.IOUScore(threshold=0.5), sm.metrics.FScore(threshold=0.5)]

        self.model.compile(optim, total_loss, metrics)


    def predict(self, pil_img):

        cv_img = np.array(pil_img) 
        cv_img = cv_img[:, :, ::-1].copy()

        image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (960,280), interpolation=cv2.INTER_LINEAR)
        preprocessing = get_preprocessing()
        sample = preprocessing(image=image)
        image = sample['image']
        image = np.expand_dims(image, axis=0)

        pr_mask = self.model.predict(image).round()
        pr_mask=pr_mask[..., 0].squeeze()

        formatted_mask = (pr_mask * 255 / np.max(pr_mask)).astype(np.uint8)
        resized_mask   = cv2.resize(formatted_mask,(cv_img.shape[1],cv_img.shape[0]))
            
        rows = np.where(resized_mask.sum(axis=1))
        if rows[0].size > 0:
            pixel_crop_height = rows[0][0]
        else:
            pixel_crop_height = int(image.shape[0]/2)

        img_crop = pil_img.crop((0,pixel_crop_height,cv_img.shape[1],cv_img.shape[0]))

        # yolo_crop.convert_annotation(xml_dir, image_dir, pixel_crop_height, out_dir)

        return img_crop