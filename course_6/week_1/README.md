# Recap
## Built-In Libraries vs. External Libraries
- Using Python Imaging Library (PIL) to transform and convert images.
- Install PIL:

  ```bash
  # PIL doesn't exists
  >>> import PIL
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ModuleNotFoundError: No module named 'PIL'

  # Download from apt
  user@ubuntu:~$ sudo apt install python3-pil
  Reading package lists... Done
  Building dependency tree     
  (...)
  Unpacking python3-pil:amd64 (4.3.0-2) ...
  Setting up python3-pil:amd64 (4.3.0-2) ...
  
  # Download from pip3
  $ pip3 install pillow
  Collecting pillow
    Downloading https://files.pythonhosted.org/packages/85/28/2c72ba965b52884a0bd71e419761fc162763dc2e5d9bec2f3b1949f7272a/Pillow-6.2.1-cp37-cp37m-macosx_10_6_intel.whl (3.9MB)
       |████████████████████████████████| 3.9MB 1.7MB/s
  Installing collected packages: pillow
  Successfully installed pillow-6.2.1
  ```
- Importing PIL:

  ```python
  import PIL
  ```
  
## What is an API?
- Application Programming Interfaces (APIs) help different pieces of software talk to each other. 
- These libraries provide APIs in the form of external or public functions, classes, and methods that other code can use to get their job done without having to create a lot of repeated code.
- For example, Cloud services use APIs that your programs can communicate with by making web calls. 
- These internal or private functions, classes, and methods do important work, but they’re there to support the functions that are published by the library
- When a library author needs to make a breaking change to an API, then they need to have a plan in place for communicating that change to their users.

## How to Make Sense of an API?
-  Well-designed API will follow patterns and naming conventions. That means that the functions, classes and methods should have names that help you understand what to expect from them. 
-  Example of using PIL:

    ```python
    from PIL import Image
    im = Image.open("bride.jpg")
    im.rotate(45).show()
    ```
- For a Python library like PIL, the code is documented using docstrings.
- PIL documentation using `help()`:

  ```bash
  >>> help(PIL)

  Help on package PIL:

  NAME
      PIL - Pillow (Fork of the Python Imaging Library)

  DESCRIPTION
      Pillow is the friendly PIL fork by Alex Clark and Contributors.
          https://github.com/python-pillow/Pillow/

      Pillow is forked from PIL 1.1.7.

      PIL is the Python Imaging Library by Fredrik Lundh and Contributors.
      Copyright (c) 1999 by Secret Labs AB.

      Use PIL.__version__ for this Pillow version.
      PIL.VERSION is the old PIL version and will be removed in the future.

      ;-)

  PACKAGE CONTENTS
      BdfFontFile
      BlpImagePlugin
      BmpImagePlugin
      BufrStubImagePlugin
      ContainerIO
      CurImagePlugin
      DcxImagePlugin
      DdsImagePlugin
      EpsImagePlugin
  ...

  ```

## How to Use PIL for Working With Images
- When using PIL, we typically create Image objects that hold the data associated with the images that we want to process. On these objects, we operate by calling different methods that either return a new image object or modify the data in the image, and then end up saving the result in a different file.
- Resize an image and save the new image with a new name:

  ```python
  from PIL import Image
  im = Image("example.jpg")
  new_im = im.resize((640,480))
  new_im.save("example_resized.jpg")
  ```
- Rotate an image:

  ```python
  from PIL import Image
  im = Image("example.jpg")
  new_im = im.rotate(90)
  new_im.save("example_rotated.jpg")
  ```
- Combined one line that rotates, resizes, and saves:

  ```python
  from PIL import Image
  im = Image("example.jpg")
  im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")
  ```
