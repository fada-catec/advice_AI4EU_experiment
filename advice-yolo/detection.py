import numpy as np
import argparse
import cv2
import os
import json

def extract_boxes_confidences_classids(outputs, confidence, width, height):
    boxes = []
    confidences = []
    classIDs = []

    for output in outputs:
        for detection in output:            
            # Extract the scores, classid, and the confidence of the prediction
            scores = detection[5:]
            classID = np.argmax(scores)
            conf = scores[classID]
            
            # Consider only the predictions that are above the confidence threshold
            if conf > confidence:
                # Scale the bounding box back to the size of the image
                box = detection[0:4] * np.array([width, height, width, height])
                centerX, centerY, w, h = box.astype('int')

                # Use the center coordinates, width and height to get the coordinates of the top left corner
                x = int(centerX - (w / 2))
                y = int(centerY - (h / 2))

                boxes.append([x, y, int(w), int(h)])
                confidences.append(float(conf))
                classIDs.append(classID)

    return boxes, confidences, classIDs


def draw_bounding_boxes(image, boxes, confidences, classIDs, idxs, colors, labels):

    out = []

    if len(idxs) > 0:
        for i in idxs.flatten():
            # extract bounding box coordinates
            x, y = boxes[i][0], boxes[i][1]
            w, h = boxes[i][2], boxes[i][3]

            # draw the bounding box and label on the image
            color = [int(c) for c in colors[classIDs[i]]]
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            text = "{}: {:.2f}".format(labels[classIDs[i]], confidences[i])

            out.append([labels[classIDs[i]], x, y, w, h, confidences[i]])

            cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return image, out


def make_prediction(net, layer_names, labels, image, confidence, threshold):
    height, width = image.shape[:2]
    
    # Create a blob and pass it through the model
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(layer_names)

    # Extract bounding boxes, confidences and classIDs
    boxes, confidences, classIDs = extract_boxes_confidences_classids(outputs, confidence, width, height)

    # Apply Non-Max Suppression
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, confidence, threshold)

    return boxes, confidences, classIDs, idxs

def norm(out_list, lab_dict, sh):

    norm_list = []

    for i in out_list:
        i[0] = lab_dict[i[0]]
        i[1] /= sh[1]
        i[2] /= sh[0]
        i[3] /= sh[1]
        i[4] /= sh[0]
        i[5] = i[5]
        
        norm_list.append(i)
    return norm_list

def getClasses(file_name):
    path = os.path.join(os.getcwd(), file_name)

    with open(path) as f:
        classes = json.load(f)

    return classes

def main(img): ###descomentar para protobuf
# def main():

    # Get optional arguments
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-w', '--weights', type=str, default='/home/lfernandez/arodriguez_ws/AI4EU/yolo-obj_best.weights', help='Path to model weights')
    # parser.add_argument('-cfg', '--config', type=str, default='/home/lfernandez/arodriguez_ws/AI4EU/yolo-obj.cfg', help='Path to configuration file')
    # parser.add_argument('-l', '--labels', type=str, default='/home/lfernandez/arodriguez_ws/AI4EU/obj.names', help='Path to label file')
    # parser.add_argument('-i', '--image_path', type=str, default='/home/lfernandez/arodriguez_ws/AI4EU/img/image1.jpg', help='Path to the image file.')
    # parser.add_argument('-c', '--confidence', type=float, default=0.2, help='Minimum confidence for a box to be detected.')
    # parser.add_argument('-t', '--threshold', type=float, default=0.3, help='Threshold for Non-Max Suppression')
    # parser.add_argument('-sh', '--show', default=True, action="store_false", help='Show output')

    # args = parser.parse_args()

    # Parameters
    show = 0
    confidence = 0.2
    threshold = 0.3

    # Path to files
    path = os.getcwd()

    config = os.path.join(path, "config", "yolo-obj.cfg")
    weights = os.path.join(path, "config", "yolo-obj_best.weights")
    names = os.path.join(path, "config", "classes.json")
    # image_path = os.path.join(path, "imgs", "1625758239020.jpg") ###comentar para protobuf

    # Get the labels
    labels_dict = getClasses(names)
    labels = []

    for i in labels_dict:
        labels.append(i)

    # Create a list of colors for the labels
    colors = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')

    # Load weights using OpenCV
    net = cv2.dnn.readNetFromDarknet(config, weights)

    # Get the ouput layer names
    layer_names = net.getLayerNames()
    layer_names = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # image = cv2.imread(image_path) ###comentar para protobuf
    image = img ###descomentar para protobuf

    boxes, confidences, classIDs, idxs = make_prediction(net, layer_names, labels, image, confidence, threshold)

    output_list = []

    image, output_list = draw_bounding_boxes(image, boxes, confidences, classIDs, idxs, colors, labels)

    # show the output image
    if show == 1:
        cv2.imshow('YOLO Object Detection', image)
        cv2.waitKey(0)


    return norm(output_list, labels_dict, image.shape)

# print(main()) ###comentar para protobuf