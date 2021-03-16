#!/usr/bin/env python3
import requests
import os

url = "http://35.222.77.149/upload/"
os.chdir("/home/student-01-58646e03997a/supplier-data/images/")

for filename in os.listdir("."):
  if not filename.endswith(".jpeg"):
      continue
  with open(filename, 'rb') as opened:
    response = requests.post(url, files={'file': opened})
    response.raise_for_status()
