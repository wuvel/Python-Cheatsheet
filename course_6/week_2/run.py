#!/usr/bin/env python3

import os
import requests

feedback_dict = {}

os.chdir("/data/feedback")
for filename in os.listdir("."):
  with open(filename) as f:
    feedback_dict['title'] = f.readline().strip()
    feedback_dict['name'] = f.readline().strip()
    feedback_dict['date'] = f.readline().strip()
    feedback_dict['feedback'] = f.readline().strip()
  response = requests.post("http://34.69.106.194/feedback/", data=feedback_dict)
  response.raise_for_status()
