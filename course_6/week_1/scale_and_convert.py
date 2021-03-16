#!/usr/bin/env python3

import os
from PIL import Image

os.chdir("/home/student-02-16635c8b85d6/images")
for filename in os.listdir("."):
    if filename == ".DS_Store":
      continue
    im = Image.open(filename)
    im.rotate(90).resize((128,128)).convert('RGB').save("/opt/icons/{}.jpeg".format(filename))
