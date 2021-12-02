import os
from tqdm import tqdm
import xml.etree.ElementTree as ET
import json
from shutil import rmtree

shared_folder = os.getenv("SHARED_FOLDER_PATH")
# shared_folder = os.path.join(os.getcwd(), 'shared_folder') #for debug

########################################### GENERIC -> YOLO

def GENERICtoYOLO(generic_format, no_attrib_flag=False):

    yolo_path = os.path.join(shared_folder, 'labels', 'yolo')

    os.makedirs(yolo_path, exist_ok=True)

    if not(no_attrib_flag):

        w = generic_format['xbr']-generic_format['xtl']
        h = generic_format['ybr']-generic_format['ytl']
        cx = generic_format['xtl'] + (w/2)
        cy = generic_format['ytl'] + (h/2)

        w /= generic_format['image_width']
        h /= generic_format['image_height']
        cx /= generic_format['image_width']
        cy /= generic_format['image_height']

        yolo_string = str(generic_format['class'])+' '+str(round(cx,3))+' '+str(round(cy,3))+' '+str(round(w,3))+' '+str(round(h,3))

        #Save YOLO txt file
        save_file_name = os.path.join(yolo_path, generic_format['filename'].replace("jpg", "txt"))

        with open(save_file_name, 'a+') as f:
            f.write(yolo_string+'\n')

    else:

        yolo_string = ''

        #Save YOLO txt file
        save_file_name = os.path.join(yolo_path, generic_format['filename'].replace("jpg", "txt"))
    
        with open(save_file_name, 'a+') as f:
            f.write(yolo_string)

########################################### CVAT -> YOLO

def CVATtoYOLO(filename, classes):

    cvat_path = os.path.join(shared_folder, 'labels', 'cvat', filename)

    root = ET.parse(cvat_path).getroot()

    for elem in tqdm(root, colour='yellow', desc='CVAT   -> YOLO'):
        if elem.tag == 'image':
            if list(elem) != []:
                for subelem in elem:

                    generic_format = CVATtoGENERIC(elem, subelem, classes)

                    GENERICtoYOLO(generic_format)

                    
            else:

                generic_format = {}
                generic_format['filename'] = elem.attrib['name']
                
                GENERICtoYOLO(generic_format, no_attrib_flag=True)            

def CVATtoGENERIC(elem, subelem, classes):

    generic_format = {}

    generic_format['filename'] = elem.attrib['name']
    generic_format['image_width'] = int(elem.attrib['width'])
    generic_format['image_height'] = int(elem.attrib['height'])

    generic_format['class_name'] = subelem.attrib['label']
    generic_format['class'] = classes[generic_format['class_name']]

    # Get coordinates
    if subelem.tag == "polygon":

        points = subelem.attrib['points'].split(';')

        x_set = []
        y_set = []

        for i in points:
            aux = i.split(',')
            x_set.append(aux[0])
            y_set.append(aux[1])
        
        generic_format['xtl'] = float(min(x_set))
        generic_format['ytl'] = float(min(y_set))
        generic_format['xbr'] = float(max(x_set))
        generic_format['ybr'] = float(max(y_set))

    elif subelem.tag == "box":
        generic_format['xtl'] = float(subelem.attrib['xtl'])
        generic_format['ytl'] = float(subelem.attrib['ytl'])
        generic_format['xbr'] = float(subelem.attrib['xbr'])
        generic_format['ybr'] = float(subelem.attrib['ybr'])

    else:
        pass # Future work if exists new tags

    return generic_format

########################################### PASCAL -> YOLO

def PASCALtoYOLO(labels_folder, classes):

    pascal_path = os.path.join(shared_folder, 'labels', labels_folder)
    annotations = [os.path.join(pascal_path, x) for x in os.listdir(pascal_path) if x[-3:] == "xml"]

    for xml_file in tqdm(annotations, colour='cyan', desc='PASCAL -> YOLO'):
        
        root = ET.parse(xml_file).getroot()

        if root.findall('object'):
            for obj in root.iter('object'):
                generic_format = PASCALtoGENERIC(root, obj, classes)
                GENERICtoYOLO(generic_format)


        else:
            generic_format = {}
            generic_format['filename'] = root.find('filename').text
            GENERICtoYOLO(generic_format, no_attrib_flag=True)

def PASCALtoGENERIC(root, obj, classes):

    generic_format = {}

    generic_format['filename'] = root.find('filename').text

    size = root.find('size')
    generic_format['image_width'] = int(size.find('width').text)
    generic_format['image_height'] = int(size.find('height').text)

    generic_format['class_name'] = obj.find('name').text
    generic_format['class'] = classes[generic_format['class_name']]

    bbox = obj.find('bndbox')
    generic_format['xtl'] = float(bbox.find('xmin').text)
    generic_format['ytl'] = float(bbox.find('ymin').text)
    generic_format['xbr'] = float(bbox.find('xmax').text)
    generic_format['ybr'] = float(bbox.find('ymax').text)

    return generic_format

########################################### COCO -> YOLO

def COCOtoYOLO(filename, classes):

    coco_path = os.path.join(shared_folder, 'labels', 'coco', filename)

    with open(coco_path) as f:
        data = json.load(f)

    use_segments = False

    images = {'%g' % x['id']: x for x in data['images']}

    categories = {'%g' % x['id']: x for x in data['categories']}

    labeled_images = []

    #Labeled images
    for elem in data['annotations']:
        
        labeled_images.append(elem['image_id'])

        generic_format = COCOtoGENERIC(elem, categories, classes, images)

        GENERICtoYOLO(generic_format)

    # Non-labeled images
    for img in tqdm(data['images'], colour = 'magenta', desc = 'COCO   -> YOLO'):
        if img['id'] not in labeled_images:

            generic_format = {}
            generic_format['filename'] = img['file_name']

            GENERICtoYOLO(generic_format, no_attrib_flag=True)
        
def COCOtoGENERIC(elem, categories, classes, images):
        
    img = images['%g' % elem['image_id']]

    generic_format = {}

    generic_format['filename'] = img['file_name']
    generic_format['image_width'] = img['width']
    generic_format['image_height'] = img['height']
    
    cat = categories['%g' % elem['category_id']]
    
    generic_format['class_name'] = cat['name']
    generic_format['class'] = classes[generic_format['class_name']]

    generic_format['xtl'] = elem['bbox'][0]
    generic_format['ytl'] = elem['bbox'][1]
    generic_format['xbr'] = round(elem['bbox'][0] + elem['bbox'][2], 3)
    generic_format['ybr'] = round(elem['bbox'][1] + elem['bbox'][3], 3)

    return generic_format

########################################### AUX

def getOpt():

    check=False
    num = 0
    while(not check):
        try:
            num = int(input('Select one option: '))
            check = True
        except ValueError:
            print('Error. Enter a number')

    return num

def getClasses(file_name):
    path = os.path.join(os.getcwd(), file_name)

    with open(path) as f:
        classes = json.load(f)

    return classes

######################################### MAIN PROTO

def main(opt):

    classes_dict = getClasses(os.path.join(shared_folder, 'classes.json'))

    if opt == "CVAT":
        if os.path.exists(os.path.join(shared_folder, 'labels', 'yolo')):  # Delete YOLO folder to create new one later
            rmtree(os.path.join(shared_folder, 'labels', 'yolo'))
        CVATtoYOLO('annotations.xml', classes_dict)
    elif opt == "PASCAL":
        if os.path.exists(os.path.join(shared_folder, 'labels', 'yolo')):
            rmtree(os.path.join(shared_folder, 'labels', 'yolo'))
        PASCALtoYOLO('pascal', classes_dict)
    elif opt == "COCO":
        if os.path.exists(os.path.join(shared_folder, 'labels', 'yolo')):
            rmtree(os.path.join(shared_folder, 'labels', 'yolo'))
        COCOtoYOLO('instances_default.json', classes_dict)
    else:
        print('Select an available option')

    return False
########################################### MAIN DEBUG

# def main():

#     classes_dict = getClasses(os.path.join(os.getcwd(), 'classes.json'))

#     exit_flag = False
#     opt = 0

#     while not exit_flag:

#         print('1. CVAT   -> YOLO')
#         print('2. PASCAL -> YOLO')
#         print('3. COCO   -> YOLO')
#         print('4. Exit')

#         opt = getOpt()

#         if opt == 1:
#             if os.path.exists(os.path.join(os.getcwd(), 'labels', 'yolo')):
#                 rmtree(os.path.join(os.getcwd(), 'labels', 'yolo'))
#             CVATtoYOLO('annotations.xml', classes_dict)
#             exit_flag = True
#         elif opt == 2:
#             if os.path.exists(os.path.join(os.getcwd(), 'labels', 'yolo')):
#                 rmtree(os.path.join(os.getcwd(), 'labels', 'yolo'))
#             PASCALtoYOLO('Annotations', classes_dict)
#             exit_flag = True
#         elif opt == 3:
#             if os.path.exists(os.path.join(os.getcwd(), 'labels', 'yolo')):
#                 rmtree(os.path.join(os.getcwd(), 'labels', 'yolo'))
#             COCOtoYOLO('instances_default.json', classes_dict)
#             exit_flag = True
#         elif opt == 4:
#             exit_flag = True
#         else:
#             print('Select an available option')

# if __name__ == "__main__":
#     main()