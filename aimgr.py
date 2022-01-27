#!/usr/bin/python3

# aimgr v 1.0 :: nevdullc :: 2022
# python tool for creating square images from a folder of images
# squared images are required for import into 'Runway' machine learning app
# *make sure to put all photos to be operated on in a folder called 'img'
# run this script from the same folder that the 'img' folder is in
# output of modified photos will be saved in newly created 'out_aimgr' folder

import os
import glob
from PIL import Image


out = 'out_aimgr'
os.makedirs(out, exist_ok=True)

files = glob.glob('./img/*')

for f in files:
    try:
        img = Image.open(f)
        img_resize = img.resize((512, 512))
        root, ext = os.path.splitext(f)
        basename = os.path.basename(root)
        img_resize.save(os.path.join(out, basename + '_mod' + ext))
    except OSError as e:
        pass

print('All modifications completed, your images_mod are in out_imgr/ ')
