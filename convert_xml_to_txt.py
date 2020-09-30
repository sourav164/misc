# scripts to convert pascal voc annotation format to yolo formate
import glob
import os
import re
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-a", "--annotation", required=True, help="Path to the annotation folder")
args = vars(ap.parse_args())
os.chdir(args["annotation"])

all_pascal_voc = glob.glob("*xml")
print ("all files - ", all_pascal_voc)


regex = re.compile('[^a-zA-Z]')
# loop through all Pascal VOC annotation file and record the location of the bounding boxes and classes
for pascal_voc in all_pascal_voc:
    xmax = []
    ymax = []
    xmin = []
    ymin = []


    # initiate writing the output yolo annotation file to write
    yolo_annotation_path = pascal_voc.replace(".xml", ".txt")
    yolo_annotation = open(yolo_annotation_path, "w")
    my_file = open(pascal_voc, "r")

    # record the location of the bounding boxes and classes
    for line in my_file:
        if "<xmax>" in line:
            xmax.append(re.findall("\d+", line)[0])
        elif "<xmin>" in line:
            xmin.append(re.findall("\d+", line)[0])
        elif "<ymax>" in line:
            ymax.append(re.findall("\d+", line)[0])
        elif "<ymin>" in line:
            ymin.append(re.findall("\d+", line)[0])

    for i in range(len(xmax)):
        entry = "cow" + " " + str(int(xmin[i])) + " " + str(int(ymin[i])  ) + " " + str(int(xmax[i])) + " " + str(int(ymax[i])) + "\n"
        yolo_annotation.write(entry)
    yolo_annotation.close()