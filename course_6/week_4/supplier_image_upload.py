#!/usr/bin/env python3
import requests
import os

url = "http://35.184.240.44/upload/"
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})

os.chdir("/home/student-02-c6bc602fd706/supplier-data/images/")
for filename in os.listdir("."):
  if not filename.endswith(".jpeg"):
      continue
  with open(filename, 'rb') as opened:
    response = requests.post(url, files={'file': opened})
    response.raise_for_status()
