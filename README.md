# Python-Cheatsheet
Handy cheat sheet for ya. Additional notes:
- [Reading and Writing Files](https://docs.python.org/3/library/functions.html#open)
- [OS Library](https://docs.python.org/3/library/os.html)
- [OS.path](https://docs.python.org/3/library/os.path.html)
- [Reading and Writing CSV](https://realpython.com/python-csv/)
- [CSV Library](https://docs.python.org/3/library/csv.html)

References: [Coursera](https://www.coursera.org/)

## String Reference 
In Python, there are a lot of things you can do with strings. In this cheat sheet, you’ll find the most common string operations and string methods.

### String operations
- len(string) Returns the length of the string
- for character in string Iterates over each character in the string
- if substring in string Checks whether the substring is part of the string
- string[i] Accesses the character at index i of the string, starting at zero
- string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.

### String methods
- string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
- string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
- string.count(substring) Returns the number of times substring is present in the string
- string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
- string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
- string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
- string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
- delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter 

## Formatting Strings 
Python offers different ways to format strings. In the video, we explained the format() method. In this reading, we'll highlight three different ways of formatting strings. For this course you only need to know the format() method. But on the internet, you might find any of the three, so it's a good idea to know that the others exist.

### Using the format() method
The format method returns a copy of the string where the {} placeholders have been replaced with the values of the variables. These variables are converted to strings if they weren't strings already. Empty placeholders are replaced by the variables passed to format in the same order.
```
# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""
```

If the placeholders indicate a number, they’re replaced by the variable corresponding to that order (starting at zero).
```
# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""
```

If the placeholders indicate a field name, they’re replaced by the variable corresponding to that field name. This means that parameters to format need to be passed indicating the field name.
```
# "{var1} {var2}".format(var1=value1, var2=value2)
"{:exp1} {:exp2}".format(value1, value2)
```

If the placeholders include a colon, what comes after the colon is a formatting expression. See below for the expression reference.
```
'{:d}'.format(10.5) → '10'
```

### Formatting expressions
| Exp | Meaning	| Example |
| --- | ------- | ------- |
| {:d}	| integer value	| '{:d}'.format(10.5) → '10'
| {:.2f} | floating point with that many decimals	 | '{:.2f}'.format(0.5) → '0.50' |
| {:.2s}	| string with that many characters	| '{:.2s}'.format('Python') → 'Py' |
| {:<6s}	| string aligned to the left that many spaces	| '{:<6s}'.format('Py') → 'Py    ' |
| {:>6s}	| string aligned to the right that many spaces	| '{:>6s}'.format('Py') → '    Py' |
| {:^6s}	| string centered in that many spaces	| '{:^6s}'.format('Py') → '  Py  ' |

More at [here](https://docs.python.org/3/library/string.html#format-specification-mini-language)

### Old string formatting 
The format() method was introduced in Python 2.6. Before that, the % (modulo) operator could be used to get a similar result. While this method is no longer recommended for new code, you might come across it in someone else's code. This is what it looks like:
```
"base string with %s placeholder" % variable
```

The % (modulo) operator returns a copy of the string where the placeholders indicated by %  followed by a formatting expression are replaced by the variables after the operator.
```
"base string with %d and %d placeholders" % (value1, value2)
```

To replace more than one value, the values need to be written between parentheses. The formatting expression needs to match the value type.
```
"%(var1) %(var2)" % {var1:value1, var2:value2}
```

Variables can be replaced by name using a dictionary syntax (we’ll learn about dictionaries in an upcoming video).
```
"Item: %s - Amount: %d - Price: %.2f" % (item, amount, price)
```

The formatting expressions are mostly the same as those of the format() method. 

### Formatted string literals 
This feature was added in Python 3.6 and isn’t used a lot yet. Again, it's included here in case you run into it in the future, but it's not needed for this or any upcoming courses.

A formatted string literal or f-string is a string that starts with 'f' or 'F' before the quotes. These strings might contain {} placeholders using expressions like the ones used for format method strings.

The important difference with the format method is that it takes the value of the variables from the current context, instead of taking the values from parameters.

Examples:
```
>>> name = "Micah"
>>> print(f'Hello {name}')
Hello Micah
>>> item = "Purple Cup"
>>> amount = 5
>>> price = amount * 3.25
>>> print(f'Item: {item} - Amount: {amount} - Price: {price:.2f}')
Item: Purple Cup - Amount: 5 - Price: 16.25
```

## Lists and Tuples Operations 
Lists and tuples are both sequences, so they share a number of sequence operations. But, because lists are mutable, there are also a number of methods specific just to lists. This cheat sheet gives you a run down of the common operations first, and the list-specific operations second.

### Common sequence operations
- len(sequence) Returns the length of the sequence
- for element in sequence Iterates over each element in the sequence
- if element in sequence Checks whether the element is part of the sequence
- sequence[i] Accesses the element at index i of the sequence, starting at zero
- sequence[i:j] Accesses a slice starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(sequence) by default.
- for index, element in enumerate(sequence) Iterates over both the indexes and the elements in the sequence at the same time

### List-specific operations and methods
- list[i] = x Replaces the element at index i with x
- list.append(x) Inserts x at the end of the list
- list.insert(i, x) Inserts x at index i
- list.pop(i) Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
- list.remove(x) Removes the first occurrence of x in the list
- list.sort() Sorts the items in the list
- list.reverse() Reverses the order of items of the list
- list.clear() Removes all the items of the list
- list.copy() Creates a copy of the list
- list.extend(other_list) Appends all the elements of other_list at the end of list

### List comprehension
- [expression for variable in sequence] Creates a new list based on the given sequence. Each element is the result of the given expression.
- [expression for variable in sequence if condition] Creates a new list based on the given sequence. Each element is the result of the given expression; elements only get added if the condition is true.  

## Dictionary Methods 
### Definition
x = {key1:value1, key2:value2} 

### Operations
- len(dictionary) - Returns the number of items in the dictionary
- for key in dictionary - Iterates over each key in the dictionary
- for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
- if key in dictionary - Checks whether the key is in the dictionary
- dictionary[key] - Accesses the item with key key of the dictionary
- dictionary[key] = value - Sets the value associated with key
- del dictionary[key] - Removes the item with key key from the dictionary

### Methods
- dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
- dict.keys() - Returns a sequence containing the keys in the dictionary
- dict.values() - Returns a sequence containing the values in the dictionary
- dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
- dict.clear() - Removes all the items of the dictionary

## Classes
### Defining Classes (Optional)
We can create and define our classes in Python similar to how we define functions. We start with the class keyword, followed by the name of our class and a colon. Python style guidelines recommend class names to start with a capital letter. After the class definition line is the class body, indented to the right. Inside the class body, we can define attributes for the class.

Let's take our Apple class example:
```
>>> class Apple:
...     color = ""
...     flavor = ""
... 
```

We can create a new instance of our new class by assigning it to a variable. This is done by calling the class name as if it were a function. We can set the attributes of our class instance by accessing them using dot notation. Dot notation can be used to set or retrieve object attributes, as well as call methods associated with the class.
```
>>> jonagold = Apple()
>>> jonagold.color = "red"
>>> jonagold.flavor = "sweet"
```

We created an Apple instance called jonagold, and set the color and flavor attributes for this Apple object. We can create another instance of an Apple and set different attributes to differentiate between two different varieties of apples.
```
>>> golden = Apple()
>>> golden.color = "Yellow"
>>> golden.flavor = "Soft"
```

We now have another Apple object called golden that also has color and flavor attributes. But these attributes have different values.

### Special Methods
Instead of creating classes with empty or default values, we can set these values when we create the instance. This ensures that we don't miss an important value and avoids a lot of unnecessary lines of code. To do this, we use a special method called a constructor. Below is an example of an Apple class with a constructor method defined.
```
>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
```

When you call the name of a class, the constructor of that class is called. This constructor method is always named __init__. You might remember that special methods start and end with two underscore characters. In our example above, the constructor method takes the self variable, which represents the instance, as well as color and flavor parameters. These parameters are then used by the constructor method to set the values for the current instance. So we can now create a new instance of the Apple class and set the color and flavor values all in go:
```
>>> jonagold = Apple("red", "sweet")
>>> print(jonagold.color)
Red
```

In addition to the __init__ constructor special method, there is also the __str__ special method. This method allows us to define how an instance of an object will be printed when it’s passed to the print() function. If an object doesn’t have this special method defined, it will wind up using the default representation, which will print the position of the object in memory. Not super useful. Here is our Apple class, with the __str__ method added:
```
>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
...     def __str__(self):
...         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
...
```

Now, when we pass an Apple object to the print function, we get a nice formatted string:
```
>>> jonagold = Apple("red", "sweet")
>>> print(jonagold)
This apple is red and its flavor is sweet
```

This apple is red and its flavor is sweet

It's good practice to think about how your class might be used and to define a `__str__` method when creating objects that you may want to print later.

### Documenting with Docstrings
The Python help function can be super helpful for easily pulling up documentation for classes and methods. We can call the help function on one of our classes, which will return some basic info about the methods defined in our class:

```
>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
...     def __str__(self):
...         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
... 
>>> help(Apple)
Help on class Apple in module __main__:

class Apple(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self, color, flavor)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __str__(self)
 |      Return str(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 ```
 
We can add documentation to our own classes, methods, and functions using docstrings. A docstring is a short text explanation of what something does. You can add a docstring to a method, function, or class by first defining it, then adding a description inside triple quotes. Let's take the example of this function:
```>>> def to_seconds(hours, minutes, seconds):
...     """Returns the amount of seconds in the given hours, minutes and seconds."""
...     return hours*3600+minutes*60+seconds
... 
>>> def to_seconds(hours, minutes, seconds):
...     """Returns the amount of seconds in the given hours, minutes and seconds."""
...     return hours*3600+minutes*60+seconds
... 
```

We have our function called to_seconds on the first line, followed by the docstring which is indented to the right and wrapped in triple quotes. Last up is the function body. Now, when we call the help function on our to_seconds function, we get a handy description of what the function does:
```
>>> help(to_seconds)
Help on function to_seconds in module __main__:

to_seconds(hours, minutes, seconds)
    Returns the amount of seconds in the given hours, minutes and seconds.
```

Docstrings are super useful for documenting our custom classes, methods, and functions, but also when working with new libraries or functions. You'll be extremely grateful for docstrings when you have to work with code that someone else wrote!

### Additional info
Classes and Instances
- Classes define the behavior of all instances of a specific class.
- Each variable of a specific class is an instance or object.
- Objects can have attributes, which store information about the object.
- You can make objects do work by calling their methods.
- The first parameter of the methods (self) represents the current instance.
- Methods are just like functions, but they can only be used through a class.

Special methods
- Special methods start and end with `__`.
- Special methods have specific names, like `__init__` for the constructor or `__str__` for the conversion to string.

Documenting classes, methods and functions
- You can add documentation to classes, methods, and functions by using docstrings right after the definition.

### Inheritance
In object-oriented programming, the concept of inheritance allows you to build relationships between objects, grouping together similar concepts and reducing code duplication. Let's create a custom Fruit class with color and flavor attributes:
```
>>> class Fruit:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
...
```

We defined a Fruit class with a constructor for color and flavor attributes. Next, we'll define an Apple class along with a new Grape class, both of which we want to inherit properties and behaviors from the Fruit class:
```
>>> class Apple(Fruit):
...     pass
... 
>>> class Grape(Fruit):
...     pass
... 
```

In Python, we use parentheses in the class declaration to have the class inherit from the Fruit class. So in this example, we’re instructing our computer that both the Apple class and Grape class inherit from the Fruit class. This means that they both have the same constructor method which sets the color and flavor attributes. We can now create instances of our Apple and Grape classes:
```
>>> granny_smith = Apple("green", "tart")
>>> carnelian = Grape("purple", "sweet")
>>> print(granny_smith.flavor)
tart
>>> print(carnelian.color)
purple
```

Inheritance allows us to define attributes or methods that are shared by all types of fruit without having to define them in each fruit class individually. We can then also define specific attributes or methods that are only relevant for a specific type of fruit. Let's look at another example, this time with animals:
```
>>> class Animal:
...     sound = ""
...     def __init__(self, name):
...         self.name = name
...     def speak(self):
...         print("{sound} I'm {name}! {sound}".format(
...             name=self.name, sound=self.sound))
... 
>>> class Piglet(Animal):
...     sound = "Oink!"
... 
>>> class Cow(Animal):
...     sound = "Moooo"
...
```

We defined a parent class, Animal, with two animal types inheriting from that class: Piglet and Cow. The parent Animal class has an attribute to store the sound the animal makes, and the constructor class takes the name that will be assigned to the instance when it's created. There is also the speak method, which will print the name of the animal along with the sound it makes. We defined the Piglet and Cow classes, which inherit from the Animal class, and we set the sound attributes for each animal type. Now, we can create instances of our Piglet and Cow classes and have them speak:
```
>>> hamlet = Piglet("Hamlet")
>>> hamlet.speak()
Oink! I'm Hamlet! Oink!
... 
>>> class Cow(Animal):
...     sound = "Moooo"
... 
>>> milky = Cow("Milky White")
>>> milky.speak()
Moooo I'm Milky White! Moooo
```

We create instances of both the Piglet and Cow class, and set the names for our instances. Then we call the speak method of each instance, which results in the formatted string being printed; it includes the sound the animal type makes, along with the instance name we assigned.

### Composition
You can have a situation where two different classes are related, but there is no inheritance going on. This is referred to as composition -- where one class makes use of code contained in another class. For example, imagine we have a Package class which represents a software package. It contains attributes about the software package, like name, version, and size. We also have a Repository class which represents all the packages available for installation. While there’s no inheritance relationship between the two classes, they are related. The Repository class will contain a dictionary or list of Packages that are contained in the repository. Let's take a look at an example Repository class definition:
```
>>> class Repository:
...      def __init__(self):
...          self.packages = {}
...      def add_package(self, package):
...          self.packages[package.name] = package
...      def total_size(self):
...          result = 0
...          for package in self.packages.values():
...              result += package.size
...          return result
```

In the constructor method, we initialize the packages dictionary, which will contain the package objects available in this repository instance. We initialize the dictionary in the constructor to ensure that every instance of the Repository class has its own dictionary.

We then define the add_package method, which takes a Package object as a parameter, and then adds it to our dictionary, using the package name attribute as the key.

Finally, we define a total_size method which computes the total size of all packages contained in our repository. This method iterates through the values in our repository dictionary and adds together the size attributes from each package object contained in the dictionary, returning the total at the end. In this example, we’re making use of Package attributes within our Repository class. We’re also calling the values() method on our packages dictionary instance. Composition allows us to use objects as attributes, as well as access all their attributes and methods.
