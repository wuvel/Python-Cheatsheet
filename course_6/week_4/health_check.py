#!/usr/bin/env python3
import psutil 
import shutil
import socket
import os
import emails

case = ""
subject = ""

# CPU usage
cpu_usage = psutil.cpu_percent()

# Disk usage
total, used, free = shutil.disk_usage("/")
free = free // (2**30)
total = (total // (2**30))*(20/100)

# Memory usage
memory_usage = psutil.virtual_memory()[1]/1024

# Hostname
host_name = socket.gethostbyname('localhost')


if cpu_usage >= 80:
  case = "CPU usage is over 80%"
  subject = "	Error - CPU usage is over 80%"
elif (free <= total):
  case = "Available disk space is lower than 20%"
  subject = "Error - Available disk space is less than 20%"
elif memory_usage <= 500000:
  case = "available memory is less than 500MB"
  subject = "Error - Available memory is less than 500MB"
elif host_name != "127.0.0.1":
  case = 'hostname "localhost" cannot be resolved to "127.0.0.1"'
  subject = "Error - localhost cannot be resolved to 127.0.0.1"

# Send email
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."

message = emails.generate_error_report(sender, receiver, subject, body)
emails.send_email(message)
