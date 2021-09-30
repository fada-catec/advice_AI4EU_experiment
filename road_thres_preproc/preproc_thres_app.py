#!/usr/bin/env python3

#########################
# @short: The following code detects and removes the sky in a set of pictures
#
# The goal is to detect the sky and remove it from the image to make
# the task easier for the DL algorithm. It is assumed that the images
# are always taken with the sky in the upper side of the picture.
#########################

import cv2
from cv2 import threshold
import preproc_thres
import os

# Asumes images are at a folder close to this system
path_imgs = "/images"

# path = os.path.dirname(__file__)
path = os.getcwd()
# path = path[0:path.rfind('/')] 
path = path + path_imgs

files = os.listdir(path)
image_files = []
# Checking if images are from the supported types
img_types = [".jpg",".png",".gif",".tiff",".psd",".bmp"]
for file in files:
    for img_type in img_types:
        if (file.find(img_type) > 0):
            image_files.append(file)

print("Running the sky remover for " + str(len(image_files)) + " files")
for i in range(0,len(image_files)):
    file = image_files[i]
    print("[" + str(i) + "/" + str(len(image_files)) + "] " + \
          "Removing sky at " + file ) 
    image = preproc_thres.Picture_Filter(path + '/' + file)
    #image.show_original(1)
    threshold =  100
    image.dynamic_detection(threshold , True)
    image.show_filter(0)
    # cv2.waitKey(0)
    
    image.apply_filter_black()
    image.show_filtered(0)
    # cv2.waitKey(0)

    image.apply_filter_cut()
    image.show_filtered(1)
    # cv2.waitKey(0)

    image.save_at(os.getcwd() + "/cropped")

    cv2.destroyAllWindows()
    










