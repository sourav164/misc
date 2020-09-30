import glob
import os
import re
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--annotation", required=True, help="Path to the annotation folder")
args = vars(ap.parse_args())
os.chdir(args["annotation"])

all_pascal_voc = glob.glob("*txt")


for pascal_voc in all_pascal_voc:
	fl_name = pascal_voc.replace(".jpg", "")
	fl_name = fl_name.replace(".png", "")
	new_file = open(os.path.join("output", fl_name), "w")
	my_file = open(pascal_voc, "r")

	for line in my_file:

	# 	data = line.split(" ")
	# 	cfd = float(data[5])*2
	# 	print (cfd)
	# 	new_file.write("cow"+ " ")
	# 	new_file.write(str(cfd)+" ")
	# 	new_file.write(data[0]+ " ")
	# 	new_file.write(data[1]+ " ")
	# 	new_file.write(data[2]+ " ")
	# 	new_file.write(data[3]+ " ")
	# 	new_file.write("\n")

		data = line.split(" ")
		new_file.write("cow"+ " ")

		new_file.write(data[1]+ " ")
		new_file.write(data[2]+ " ")
		new_file.write(data[3]+ " ")
		new_file.write(data[4]+ " ")
		new_file.write(data[5])
		new_file.write("\n")


	my_file.close(), new_file.close()