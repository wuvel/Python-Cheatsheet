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

## Unit Testing Library
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

## Other Test Types
**Black-box** tests are written with an awareness of what the program is supposed to do, its requirements or specifications, but not how it does it. Black-box tests are useful because they don't rely on the knowledge of how the system works.

**White-box** tests are helpful because a test writer can use their knowledge of the source code to create tests that cover most of the ways that the program behaves.

**Integration tests** verify that the interactions between the different pieces of code in integrated environments are working the way we expect them to. 

**Regression tests** usually written as part of a debugging and troubleshooting process to verify that an issue or error has been fixed once it's been identified. Regression tests are useful part of a test suite because they ensure that the same mistake doesn't happen twice.

When writing software **smoke test** serve as a kind of sanity check to find major bugs in a program. Smoke test answer basic questions like, does the program run? These tests are usually run before more refined testing takes place.

**Load tests** verify that the system behaves well when it's under significant load. To actually perform these tests will need to generate traffic to our application simulating typical usage of the service.

## Test-Driven Development
**Test-driven development** or TDD calls for creating the test before writing the code. When presented with a new problem that can be solved by automation, your gut instinct might be to fire up your code editor and start writing.

## More about tests
Check out the following links for more information:
- [https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/](https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/)
- [https://landing.google.com/sre/sre-book/chapters/testing-reliability/](https://landing.google.com/sre/sre-book/chapters/testing-reliability/)
- [https://testing.googleblog.com/2007/10/performance-testing.html](https://testing.googleblog.com/2007/10/performance-testing.html)
- [https://www.guru99.com/smoke-testing.html](https://www.guru99.com/smoke-testing.html)
- [https://www.guru99.com/exploratory-testing.html](https://www.guru99.com/exploratory-testing.html)
- [https://testing.googleblog.com/2008/09/test-first-is-fun_08.html](https://testing.googleblog.com/2008/09/test-first-is-fun_08.html)

## Try-except
```
def character_frequency(filename):
  """Counts the frequency of each character in the given file."""
  # First try to open the file
  try:
    f = open(filename)
  except OSError:
    return None

  # Process the file
  characters = {}
  for line in f:
    for char in line:
      character[char] = characters.get(char, 0) + 1
  f.close()
  return characters
```

## Raise an Error
```
def validate_user(username, minlen):
  # Using assertion
  assert type(username) == str, "username must be a string"
  
  # Using raise
  if minlen < 1:
    raise ValueError("minlen must be at least 1")
  
  # Using return
  if len(username) < minlen:
    return False
  if not username.isalnum():
    return False
  return True
 ```
We should use raise to check for conditions that we expect to happen during normal execution of our code and assert to verify situations that aren't expected but that might cause our code to misbehave.

## Testing for Expected Errors
```
#!/usr/bin/env python3

import unittest

from validations
import validate_user

class TestValidateUser(unittest, TestCase):
  def test_valid(self):
    self.assertEqual(validate("validuser", 3), True)

  def test_too_short(self):
    self.assertEqual(validate("inv", 5), False)

  def test_invalid_characters(self):
    self.assertEqual(validate("invalid_user", 1), False)

  def test_invalid_minlen(self):
    self.assertRaises(ValueError, validate_user, "user", -1)

# Run the tests
unittest.main()
```

## Re-cap Handling Errors
Raise allows you to throw an exception at any time.
- [https://docs.python.org/3/tutorial/errors.html#raising-exceptions](https://docs.python.org/3/tutorial/errors.html#raising-exceptions)

Assert enables you to verify if a certain condition is met and throw an exception if it isn’t.
- [https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
- [https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python](https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python)

The standard library documentation is kind of unclear. Basically `assert <something false>` will raise AssertionError, which the caller may need to handle.

In the try clause, all statements are executed until an exception is encountered.
- [https://docs.python.org/3/tutorial/errors.html#handling-exceptions](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)

Except is used to catch and handle the exception(s) that are encountered in the try clause.
- [https://docs.python.org/3/library/exceptions.html#bltin-exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)

Other interesting Exception handling readings:
- [https://doughellmann.com/blog/2009/06/19/python-exception-handling-techniques/](https://doughellmann.com/blog/2009/06/19/python-exception-handling-techniques/)
