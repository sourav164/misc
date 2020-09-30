import os
import glob, argparse
from PIL import Image


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image folder")
args = vars(ap.parse_args())
os.chdir(args["image"])

all_png_image = glob.glob("*png")
if not os.path.exists("output"):
    os.makedirs("output")

for png_image in all_png_image:
	im = Image.open(png_image)

	if not im.mode == 'RGB':
		im = im.convert('RGB')

	jpg_name = os.path.join("output", png_image.replace("png", "jpg"))
	im.convert('RGB').save(jpg_name)