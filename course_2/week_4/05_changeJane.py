#!/usr/bin/env python3

import sys
import subprocess
import os

filename = sys.argv[1]

if os.path.exists(filename):
    with open(filename) as f:
        line = f.readlines()
        for res in line:
            result = res.strip()
            result_new = result.replace("jane", "jdoe")
            subprocess.run(["mv", result, result_new])
    f.close()
