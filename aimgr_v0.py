#!/usr/bin/env python3
""" image resizing tool for feeding multiple resized, (squared), images to A.I. """
import os
import glob
from PIL import Image

out = 'out_aimgr'
os.makedirs(out, exist_ok=True)

files = glob.glob('./img/*')

for f in files:
    try:
        img = Image.open(f)
        width, height = img.size
        if width > height: # landscape
            aspect_ratio = height / width
            img_resize = img.resize((512, int(512 * aspect_ratio)))
        else: # portrait
            aspect_ratio = width / height
            img_resize = img.resize((int(512 * aspect_ratio), 512))
        
        root, ext = os.path.splitext(f)
        basename = os.path.basename(root)
        img_resize.save(os.path.join(out, basename + '_mod' + ext))
    except OSError as e:
        pass

print('All modifications completed, your images_mod are in out_imgr/ ')
