Table of Contents
-----------------

  * Data Streams
    * Practice Quiz: Data Streams <br>
        * `01_data_streams.ipynb`
  * Python Subprocesses
    * Practice Quiz: Python Subprocesses <br>
        * `02_python_subprocesses.ipynb`
  * Processing Log Files
    * Practice Quiz: Processing Log Files <br>
        * `03_processing_log_files.ipynb`
  * Module Review
    * Qwiklabs Assessment: Working with Log Files <br>
        * `04_find_error.py`

# Cheat sheet 
## Data Streams
### Reading Data interactively
Using `input`. Example:
```python
#!/usr/bin/env python3

name = input("What is your name: ")
print("Hello {}!".format(name))

"""Outputs:
What is your name: fikri
Hello fikri!
"""
```

### Standard Streams
I/O Streams are the basic mechanism  for performing input and output operations in programs.

| I/O Streams | Common name | 
| ----------- | ----------- |
| standard input | STDIN | 
| standard output | STDOUT |
| standard error | STDERR | 

### Environment Variables
Display all the environment variables:
```bash
$ env
```

Display the PATH variable:
```bash
$ echo $PATH
```

Python-way to get the environment variables:
```python
#!/usr/bin/env python3

import os

print("HOME: " + os.environ.get("HOME", ""))
print("HOME: " + os.environ.get("BAD", ""))

"""Outputs:
HOME: /root
HOME: 
"""
```
The `get` method from environ will return the value of the first parameter variable or the second parameter if the variable did not exists.

### Set the Environment Variable
```bash
$ export <name>=<value>
$ export BAD=Hello
```

### Print the Arguments
```python
#!/usr/bin/env python3

import sys

print(sys.argv)

"""Input and outputs:
$ ./hello.py
['./hello.py']

$ ./hello.py a b c
['./hello.py', 'a', 'b', 'c']
"""
```

### Exit Status
Checking the exit status of a program:
```bash
$ echo "Test"
$ echo $?
0 
```
| Status Code | Means | 
| ----------- | ----- |
| 0 | The program run successfuly |
| 1 | The program contains an error |

### Defining Exit Status Code with Python
```python
import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
  with open(filename, "w") as f:
    f.write("New file created\n")
else:
  print("Error! File {} already exists!".format(filename))
  sys.exit(1)

"""Input and outputs:
$ ./create_file.py test
$ echo $?
0
$ ./create_file.py test
Error! File test already exists!
$ echo $?
1
"""
```

### More About Input Functions
There are some subtle differences in how data streams are handled in Python 3 and older versions, such as Python 2. Let’s just focus on input() and raw_input(), because they work differently in Python 2 and 3, and you would want to use one or the other depending on the Python version.

In Python 2, taking an input from a user, raw_input should be used:
```bash
>>> my_number = raw_input('Please Enter a Number: \n')
Please Enter a Number: 
1337
>>> print(my_number)
1337
>>>
```
Now, this is important, because, raw_input does not evaluate an otherwise valid Python expression. In simple terms, raw_input will just get a string from a user, where input will actually perform basic maths and the like. See below:
```bash
>>> my_raw_input = raw_input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1  # This is treated like a raw string.
>>> my_input = input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1 # This is treated like an expression.
>>> print(my_raw_input)
123 + 1
>>> print(my_input)
124 # See that the expression was evaluated!
```
In Python 2 input(x) is just eval(raw_input(x)). eval() will just evaluate a generic string as if it were a Python expression.

In Python 3, taking an input from a user, input should be used. See the below sample:
```bash
>>> my_number = input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1
>>> print(my_number)
123 + 1
>>> type(my_number)
<class 'str'>
```

Notice that the expression is treated just like a string. It is not evaluated. If we want to, we can call eval() and that will actually execute the string as an expression:
```bash
>>> my_number = input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1
>>> print(my_number)
123 + 1
>>> eval(my_number)
124
```
It’s worth noting, raw_input doesn’t natively exist in Python 3, but there are some tricky ways to force the interpreter to evaluate raw_input in backwards compatible ways. This can be useful for modernizing legacy Python code without rewriting large portions of it. Research on this topic is better left to the reader, as there are lots of fun (and sometimes scary) ways of doing this.

| Python 2 | Python 3 |
| -------- | -------- |
| input(x) is roughly the same as eval(raw_input(x)) | Input handles string as a generic string. It does not evaluate the string as a string expression |
| raw_input() is preferred, unless the author wants to support evaluating string expressions | raw_input doesn’t exist, but with some tricky techniques, it can be supported | 
| eval() is used to evaluate string expressions | eval() can be used the same as Python 2 |

## Python Subprocesses
More at:
- [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
### Running System Command in Python
```bash
>>> import subprocess
>>> subprocess.run(["date"])
Tue 07 Jan 2020 02:34:44 PM PST
CompletedProcess(args=['date'], returncode=0)
>>> subprocess.run(["sleep", "2"])
CompletedProcess(args=['sleep', '2'], returncode=0)
>>> result = subprocess.run(["ls", "not_a_valid_file"])
ls: cannot access 'not_a_valid_file': No such file or directory
>>> print(result.returncode)
2
```
The return code will return after the command successfully executed.

### Obtaining the Output of a System Command
```bash
>>> import subprocess
>>> result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
>>> print(result.returncode)
0
>>> print(result.stdout.decode().split())
['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']

>>> result = subprocess.run(["rm", "abcdef"], capture_output=True)
>>> print(result.returncode)
1
>>> print(result.stdout)
b''
>>> print(result.stderr
b"rm: cannot remvoe 'abcdef': No such file or directory\n"
```

## Processing Log Files
Example of extracting the date, time, and process id from the passed line, and return this format: `Jul 6 14:01:23 pid:29440`.
```python
import re
def show_time_of_pid(line):
  pattern = r'([\w :]+[0-9\:]).*\[([0-9]+)\]'
  result = re.search(pattern, line)
  return "{} pid:{}".format(result[1], result[2])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440

"""Outputs:
Jul 6 14:01:23 pid:29440
Jul 6 14:02:08 pid:29187
Jul 6 14:02:09 pid:29187
Jul 6 14:03:01 pid:29440
Jul 6 14:03:40 pid:29807
Jul 6 14:04:01 pid:29440
Jul 6 14:05:01 pid:29440
"""
```
