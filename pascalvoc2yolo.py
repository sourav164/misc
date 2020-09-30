# scripts to convert pascal voc annotation format to yolo formate
import glob
import os
import re
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-a", "--annotation", required=True, help="Path to the annotation folder")
ap.add_argument("-m", "--method", required=False, help="default normal, put nn for non-normalize box location")
args = vars(ap.parse_args())
os.chdir(args["annotation"])

all_pascal_voc = glob.glob("*xml")
print ("all files - ", all_pascal_voc)


# for multiclass object annotation, add the classes into the dictionary 
CLASS_MAPPING = {
    "cow" : "0"
    # add your classes here -  "dog":"1"
    }
regex = re.compile('[^a-zA-Z]')
# loop through all Pascal VOC annotation file and record the location of the bounding boxes and classes
for pascal_voc in all_pascal_voc:
    xmax = []
    ymax = []
    xmin = []
    ymin = []
    object_classes = []

    # initiate writing the output yolo annotation file to write
    yolo_annotation_path = pascal_voc.replace(".xml", ".txt")
    yolo_annotation = open(yolo_annotation_path, "w")
    my_file = open(pascal_voc, "r")

    # record the location of the bounding boxes and classes
    for line in my_file:
        if "<width>" in line:
            im_width = re.findall("\d+", line)[0]
        elif "<height>" in line:
            im_height = re.findall("\d+", line)[0]
        elif "<name>" in line:
            classes = regex.sub('', line).replace('name', '')
            object_classes.append(classes)
        elif "<xmax>" in line:
            xmax.append(re.findall("\d+", line)[0])
        elif "<xmin>" in line:
            xmin.append(re.findall("\d+", line)[0])
        elif "<ymax>" in line:
            ymax.append(re.findall("\d+", line)[0])
        elif "<ymin>" in line:
            ymin.append(re.findall("\d+", line)[0])

    # get image width and height of the image from the Pascal VOC annotation file
    im_width, im_height = int(im_width), int(im_height)

    # write object class and location in the following format. Both the image width and height will be converted to 1
    # <object-class> <center x> <center y> <width> <height>
    for i in range(len(object_classes)):
        object_class = CLASS_MAPPING[object_classes[i]]
        xmaxi = int(xmax[i])
        xmini = int(xmin[i])
        ymaxi = int(ymax[i])
        ymini = int(ymin[i])

        if args["method"]=="nn":
            width = int(xmaxi) - int(xmini)
            height = int(ymaxi) - int(ymini)
            x_center = int (int(xmini) + 0.5 * width)
            y_center = int (int(ymini) + 0.5 * height)

        else:
            width = (int(xmaxi) - int(xmini)) / im_width
            height = (int(ymaxi) - int(ymini)) / im_height
            x_center = int(xmini) / im_width + 0.5 * width
            y_center = int(ymini) / im_height + 0.5 * height        	

        width, height, x_center, y_center = round(width, 3), round(height, 3), round(x_center, 3), round(y_center, 3)
        entry = "cow" + " " + str(x_center) + " " + str(y_center) + " " + str(width) + " " + str(height) + "\n"
        yolo_annotation.write(entry)
    yolo_annotation.close()