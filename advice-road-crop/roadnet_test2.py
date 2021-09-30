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
from roadnet.data_loader import Dataset, Dataloder
from roadnet.data_aug import get_training_augmentation, get_preprocessing, get_validation_augmentation
from roadnet.net import roadnet_rt

import convert_voc_to_yolo_crop as yolo_crop

def roadnet(image_orig):
    
    DATA_DIR = '/imgs/'
    x_test_dir = DATA_DIR
    y_test_dir = DATA_DIR

    config_path = "./roadnet/config.json"
    with open(config_path) as config_buffer:
        config = json.loads(config_buffer.read())

    BACKBONE = config["model"]["BACKBONE"]
    CLASSES = config["model"]["CLASSES"].split("delimiter")
    BATCH_SIZE = config["train"]["BATCH_SIZE"]
    LR = config["train"]["LR"]
    EPOCHS = config["train"]["EPOCHS"]
    HEIGHT = 280 #352
    WIDTH = 960 #1216
    # HEIGHT = config["model"]["IN_HEIGHT"]
    # WIDTH = config["model"]["IN_WIDTH"]
    path_test_weight = './roadnet_rt_9257.hdf5'
    path_cmp_weight = './roadnet_rt_9257.hdf5'

    # preprocess_input = sm.get_preprocessing(BACKBONE)

    test_dataset = Dataset(
        x_test_dir,
        y_test_dir,
        shape=(WIDTH, HEIGHT),
        classes=CLASSES,
        preprocessing=get_preprocessing() # , add_location='ch_xy_352.npy'
    )

    test_dataloader = Dataloder(test_dataset, batch_size=1, shuffle=False)

    n_classes = 1 if len(CLASSES) == 1 else (len(CLASSES) + 1)  # case for binary and multiclass segmentation
    activation = 'sigmoid' if n_classes == 1 else 'softmax'
    add_location = False
    add_crop = False
    model = roadnet_rt((HEIGHT, WIDTH), n_classes, activation).build()
    model.summary()
    metrics = [sm.metrics.IOUScore(threshold=0.5), sm.metrics.FScore(threshold=0.5)]

    # load test weights
    model.load_weights('./roadnet_rt_9257.hdf5')

    optim = keras.optimizers.Adam(LR)
    dice_loss = sm.losses.DiceLoss()
    focal_loss = sm.losses.BinaryFocalLoss() if n_classes == 1 else sm.losses.CategoricalFocalLoss()
    total_loss = dice_loss + (1 * focal_loss)

    model.compile(optim, total_loss, metrics)

    test_img_list = os.listdir(x_test_dir)

    for i,image_dir in zip(range(len(test_img_list)),test_img_list):
        
        image, gt_mask = test_dataset[i]
        image = np.expand_dims(image, axis=0)
        pr_mask = model.predict(image).round()
        pr_mask=pr_mask[..., 0].squeeze()

        formatted = (pr_mask * 255 / np.max(pr_mask)).astype(np.uint8)
        formatted2 = cv2.resize(formatted,(1280,720))
        
        rows = np.where(formatted2.sum(axis=1))
        if rows[0].size > 0:
            pixel_crop_height = rows[0][0]
        else:
            pixel_crop_height = int(image_orig.shape[0]/2)

        img_crop = image_orig.crop((0,pixel_crop_height,1280,720))

        return img_crop
