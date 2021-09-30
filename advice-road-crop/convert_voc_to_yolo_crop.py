import glob
import os
import pickle
import xml.etree.ElementTree as ET
from os import listdir, getcwd
from os.path import join

classes = ['Cracking']
# classes = ['Rutting', 'Pothole', 'ManholeCover', 'Gully', 'EdgeDeterioration', 'Cracking']


# Rutting:128,0,0::
# Pothole:0,128,0::
# ManholeCover:128,128,0::
# Gully:0,0,128::
# EdgeDeterioration:128,0,128::
# Cracking

# pixel_crop_height = 400

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(in_dir, image_name, pixel_crop_height, out_dir):
    basename = os.path.basename(image_name)
    basename_no_ext = os.path.splitext(basename)[0]

    in_file = open(in_dir + '/' + basename_no_ext + '.xml')
    out_file = open(out_dir + '/' + basename_no_ext + '.txt', 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text) - pixel_crop_height

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')

        xmin = float(xmlbox.find('xmin').text)
        xmax = float(xmlbox.find('xmax').text)
        ymin = float(xmlbox.find('ymin').text) - pixel_crop_height
        if ymin < 0:
            ymin = 0 
        ymax = float(xmlbox.find('ymax').text) - pixel_crop_height

        b = (xmin, xmax, ymin, ymax)
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

