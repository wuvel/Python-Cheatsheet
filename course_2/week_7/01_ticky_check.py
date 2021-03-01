#!/usr/bin/env python3

import re
import operator

error = {}
per_user_info = {}
per_user_error = {}
per_user = {}

# Processing the log
with open("syslog.log") as f:
    line = f.readlines()
    for res in line:
        result = res.strip()

        # Info
        re_result = re.match(r".*ticky: INFO .* \(([\w.-]+)\)$", result)
        if(re_result is not None):
            name = re_result.group(1)
            if(name not in per_user_info):
                per_user_info[name] = 1
            else:
                per_user_info[name] += 1
        
        # Error
        re_result = re.match(r".*ticky: ERROR .* \(([\w.-]+)\)$", result)
        if(re_result is not None):
            name = re_result.group(1)
            if(name not in per_user_error):
                per_user_error[name] = 1
            else:
                per_user_error[name] += 1
        
        # Error messages   
        re_result = re.match(r".*ticky: ERROR ([\w ']+) \(.*", result)
        if(re_result is not None):
            name = re_result.group(1)
            if(name not in error):
                error[name] = 1
            else:
                error[name] += 1

    error = sorted(error.items(), key = operator.itemgetter(1), reverse=True)

f.close()

# Sorting
for key, values in per_user_info.items():
    if key not in per_user:
        per_user[key] = list()
    per_user[key].append(values)

for key, values in per_user_error.items():
    if key not in per_user:
        per_user[key] = list()
    if(not per_user[key]):
        per_user[key].append(0)
    per_user[key].append(values)

per_user = sorted(per_user.items())

# Generating csv
with open("error_message.csv", "w") as file:
    file.write("Error, Count\n")
    for line in error:
        file.write("{}, {}\n".format(line[0], line[1]))
    
with open("user_statistics.csv", "w") as file:
    file.write("Username, INFO, ERROR\n")
    for line in per_user:
        try:
            file.write("{}, {}, {}\n".format(line[0], line[1][0], line[1][1]))
        except IndexError:
            file.write("{}, {}, {}\n".format(line[0], line[1][0], 0))


