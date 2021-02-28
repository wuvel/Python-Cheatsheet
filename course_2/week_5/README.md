## Simple Test
Software testing is a process of evaluating computer code to determine whether or not it does what you expect it to do. 

The most basic way of testing a script is to run it with different parameters and see if it returns the expected values. We've done this **manual testing** for some of the code that we've written this course already. Executing a script with different command-line arguments to see how its behavior changed is an example of manual testing.

Instead of us humans running a function over and over with different parameters and checking the results are what we expected them to be, we let the computer do this for us. **Automatic testing** means we'll write code to do the test. Why would you write more code to test code you have? Because when you're testing your code, you want to check if it does what it's supposed to do for a lot of different values.

## Unit Test
Unit tests are used to verify that small isolated parts of a program are correct. Unit tests are generally written alongside the code to test the behavior of individual pieces or units like functions or methods. Unit tests help assure the developer that each piece of code does what it's meant to do. When testing a function or method, we want to make sure that we're focusing on checking that the code in that function or method behaves correctly.

The goal of the unit test is to verify that small, isolated parts of a program are correct.

## Writing Unit Tests in Python
```
#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lavelace"
    self.assertEqual(rearrange_name(testcase), expected)

unittest.main()

"""Input and outputs:
$ ./rearrange_test.py
.----------------------------------------------------------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""
```

## Edge Case
**Edge cases** are inputs to our code that produce unexpected results, and are found at the extreme ends of the ranges of input we imagine our programs will typically work with. Edge cases usually need special handling in scripts in order for the code to continue to behave correctly. In our rearranging example, we can handle this edge case by performing a simple check of the result variable before operating with it.

Example:
```
#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lavelace"
    self.assertEqual(rearrange_name(testcase), expected)
    
  def test_empty(self):
    testcase = ""
    expected = ""
    self.assertEqual(rearrange_name(testcase), expected)

unittest.main()

"""Input and outputs:
$ ./rearrange_test.py
.----------------------------------------------------------------------------------------------------------------------
ERROR test_empty .....

FAILED (errors=1)
"""
```

## Recap
Best of Unit Testing Standard Library Module
Understand a Basic Example:
- [https://docs.python.org/3/library/unittest.html#basic-example](https://docs.python.org/3/library/unittest.html#basic-example)

Understand how to run the tests using the Command Line:
- [https://docs.python.org/3/library/unittest.html#command-line-interface](https://docs.python.org/3/library/unittest.html#command-line-interface)

Understand various Unit Test Design Patterns:
- [https://docs.python.org/3/library/unittest.html#organizing-test-code](https://docs.python.org/3/library/unittest.html#organizing-test-code)
- Understand the uses of setUp, tearDown; setUpModule and tearDownModule

Understand basic assertions:

| Method | Checks that | New in |
| ------ | ----------- | ------ |
| assertEqual(a, b)	| a == b | |
| assertNotEqual(a, b) | a != b	| |
| assertTrue(x)	| bool(x) is True	| |
| assertFalse(x) | bool(x) is False	| |
| assertIs(a, b) | a is b	| 3.1 |
| assertIsNot(a, b) | a is not b | 3.1 |
| assertIsNone(x) | x is None |	3.1 |
| assertIsNotNone(x) | x is not None | 3.1 | 
| assertIn(a, b) | a in b |	3.1 |
| assertNotIn(a, b)	| a not in b | 3.1 |
| assertIsInstance(a, b) | isinstance(a, b) |	3.2 |
| assertNotIsInstance(a, b) | not isinstance(a, b) | 3.2 |
