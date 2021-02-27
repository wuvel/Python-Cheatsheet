### Reading Data interactively
Using `input`. Example:
```
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
```
$ env
```

Display the PATH variable:
```
$ echo $PATH
```

Python-way to get the environment variables:
```
#!/usr/bin/env python3

import os

print("HOME: " + os.environ.get("HOME", ""))
print("HOME: " + os.environ.get("BAD", ""))

"""Outputs:
HOME: /root
HOME: 
"""
```
The `get` method from environ will return the value of the first parameter variable or the second parameter if the variable did not exist.

### Set the Environment Variable
```
$ export <name>=<value>
$ export BAD=Hello
```
