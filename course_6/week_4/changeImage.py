#!/usr/bin/env python3

import os
from PIL import Image

path = "/home/student-01-58646e03997a/supplier-data/images/"
os.chdir(path)
for filename in os.listdir("."):
    if not filename.endswith(".tiff"):
      continue
    im = Image.open(filename)
    splitted_filename = filename.split(".")
    im.resize((600,400)).convert('RGB').save("{}{}.jpeg".format(path, splitted_filename[0]))
