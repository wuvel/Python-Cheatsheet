#!/usr/bin/env python
import subprocess
import os
from multiprocessing import Pool

src = os.getcwd() + "/data/prod/"
dest = os.getcwd() + "/data/prod_backup/"

def run(task):
  subprocess.call(["rsync", "-arq", src, dest])

tasks = ['task1', 'task2', 'task3']
p = Pool(len(tasks))
p.map(run, tasks)