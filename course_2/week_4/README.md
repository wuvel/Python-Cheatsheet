## Data Streams
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
The `get` method from environ will return the value of the first parameter variable or the second parameter if the variable did not exists.

### Set the Environment Variable
```
$ export <name>=<value>
$ export BAD=Hello
```

### Print the Arguments
```
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
```
$ echo "Test"
$ echo $?
0 
```
| Status Code | Means | 
| ----------- | ----- |
| 0 | The program run successfuly |
| 1 | The program contains an error |

### Defining Exit Status Code with Python
```
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
```
>>> my_number = raw_input('Please Enter a Number: \n')
Please Enter a Number: 
1337
>>> print(my_number)
1337
>>>
```
Now, this is important, because, raw_input does not evaluate an otherwise valid Python expression. In simple terms, raw_input will just get a string from a user, where input will actually perform basic maths and the like. See below:
```
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
```
>>> my_number = input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1
>>> print(my_number)
123 + 1
>>> type(my_number)
<class 'str'>
```

Notice that the expression is treated just like a string. It is not evaluated. If we want to, we can call eval() and that will actually execute the string as an expression:
```
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
