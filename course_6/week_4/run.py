#!/usr/bin/env python3

import os
import requests

fruits_dict = {}

os.chdir("/home/student-02-c6bc602fd706/supplier-data/descriptions")
for filename in os.listdir("."):
  splitted_filename = filename.split(".")
  with open(filename) as f:
    fruits_dict['name'] = f.readline().strip()
    converted_weight = f.readline().strip().split(" ")
    fruits_dict['weight'] = int(converted_weight[0])
    fruits_dict['description'] = f.readline().strip()
    fruits_dict['image_name'] = splitted_filename[0]+".jpeg"
  response = requests.post("http://35.184.240.44/fruits/", data=fruits_dict)
  response.raise_for_status()
