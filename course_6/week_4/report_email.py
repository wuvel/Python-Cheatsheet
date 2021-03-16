#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails

fruits_dict = {}
fruits_array = list()

os.chdir("/home/student-02-c6bc602fd706/supplier-data/descriptions")
for filename in os.listdir("."):
  with open(filename) as f:
    fruits_dict['name'] = f.readline().strip()
    fruits_dict['weight'] = f.readline().strip()
    f.readline().strip()
    fruits_array.append("name: {}\nweight: {}\n".format(fruits_dict['name'], fruits_dict['weight']))

# Get Today Date
today = date.today()
formatted_date = today.strftime("%B %d, %Y")
title_date = "Processed Update on {}".format(formatted_date)

if __name__ == "__main__":
  body_pdf = ""
  body_email = ""

  # Formatted summary
  for s in fruits_array:
    body_pdf += s + "<br/><br/>"
    body_email += s + "\n\n"

  reports.generate_report("/tmp/processed.pdf", title_date, body_pdf)

  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = body_email

  message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send_email(message)
    
