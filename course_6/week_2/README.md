# Recap
## Web Applications and Services
- A web application is an application that you interact with over HTTP.
- Your web browser sends an HTTP request to a web server. Then, the web server passes the request along to the web application in charge of deciding what information to show you. The application then generates the website content (in HTML format).
- Web applications that have an API are also known as web services.
- Instead of browsing to a web page to type and click around, you can use your program to send a message known as an API call to the web service. The part of the program that listens on the network for API calls is called an API endpoint.
- Data serialization is the process of taking an in-memory data structure, like a Python object, and turning it into something that can be stored on disk or transmitted across a network. Later, the file can be read, or the network transmission can be received by another program and turned back into an object again. 
- Turning the serialized object back into an in-memory object is called deserialization.
- A web service's API endpoint takes messages in a specific format, containing specific data. 
- Instead of having a list of lists, we could turn this information into a list of dictionaries. In each of these dictionaries, the key will be the name of the column, and the value will be the corresponding information in each row. 

  ```python
  people = [
      {
          "name": "Sabrina Green",
          "username": "sgreen",
          "phone": "802-867-5309",
          "department": "IT Infrastructure",
          "role": "Systems Administrator"
      },
      {
          "name": "Eli Jones",
          "username": "ejones",
          "phone": "684-348-1127",
          "department": "IT Infrastructure",
          "role": "IT Specialist"
      },
  ]
  ```
- Using a structure like this lets us do interesting things with our information that’s much harder to do with CSV files. For example, let's say we want to record more than one phone number for each person. Instead of using a single string for "phone", we could represent that data in another dictionary, like this:  

  ```python
  people = [
      {
          "name": "Sabrina Green",
          "username": "sgreen",
          "phone": {
              "office": "802-867-5309",
              "cell": "802-867-5310"
          },
          "department": "IT Infrastructure",
          "role": "Systems Administrator"
      },
      {
          "name": "Eli Jones",
          "username": "ejones",
          "phone": {
              "office": "684-348-1127"
          },
          "department": "IT Infrastructure",
          "role": "IT Specialist"
      },
  ]
  ```
  
## Data Serialization Formats
- JSON (JavaScript Object Notation) is the serialization format.
- Use the json module to convert our people list of dictionaries into JSON format.  

  ```python
  import json

  with open('people.json', 'w') as people_json:
      json.dump(people, people_json, indent=2)
  ```
  This code uses the json.dump() function to serialize the people object into a JSON file. The contents of the file will look something like this:  
  
  ```
  [
    {
      "name": "Sabrina Green",
      "username": "sgreen",
      "phone": {
        "office": "802-867-5309",
        "cell": "802-867-5310"
      },
      "department": "IT Infrastructure",
      "role": "Systems Administrator"
    },
    {
      "name": "Eli Jones",
      "username": "ejones",
      "phone": {
        "office": "684-348-1127"
      },
      "department": "IT Infrastructure",
      "role": "IT Specialist"
    },
  ]
  ```
- YAML (Yet Another Markup Language) has a lot in common with JSON. They’re both formats that can be easily understood by a human when looking at the contents.
- Using the yaml.safe_dump() method to serialize our object into YAML:  

  ```python
  import yaml

  with open('people.yaml', 'w') as people_yaml:
      yaml.safe_dump(people, people_yaml)
  ```
  That code will generate a people.yaml file that looks like this: 
  
  ```
  - department: IT Infrastructure
  name: Sabrina Green
  phone:
    cell: 802-867-5310
    office: 802-867-5309
  role: Systems Administrator
  username: sgreen
  - department: IT Infrastructure
  name: Eli Jones
  phone:
    office: 684-348-1127
  role: IT Specialist
  username: ejones
  ```
## More About JSON
- JSON is human-readable, which means it’s encoded using printable characters, and formatted in a way that a human can understand.
- JSON supports a few elements of different data types.
- JSON 101:

  ```json
  # String
  "Sabrina Green"

  # Number
  1002

  # Objects, which are key-value pair structures like Python dictionaries.  
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "uid": 1002
  }

  # key-value pair can contain another object as a value.  
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "uid": 1002,
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    }
  }

  # arrays, which are equivalent to Python lists.
  [
    "apple",
    "banana",
    12345,
    67890,
    {
      "name": "Sabrina Green",
      "username": "sgreen",
      "phone": {
        "office": "802-867-5309",
        "cell": "802-867-5310"
      },
      "department": "IT Infrastructure",
      "role": "Systems Administrator"
    }
  ]
  ```
- JSON elements are always comma-delimited.
- The json library will help us turn Python objects into JSON, and turn JSON strings into Python objects! The dump() method serializes basic Python objects, writing them to a file. Like in this example:  

  ```python
  import json

  people = [
    {
      "name": "Sabrina Green",
      "username": "sgreen",
      "phone": {
        "office": "802-867-5309",
        "cell": "802-867-5310"
      },
      "department": "IT Infrastructure",
      "role": "Systems Administrator"
    },
    {
      "name": "Eli Jones",
      "username": "ejones",
      "phone": {
        "office": "684-348-1127"
      },
      "department": "IT Infrastructure",
      "role": "IT Specialist"
    }
  ]

  with open('people.json', 'w') as people_json:
      json.dump(people, people_json)
  ```
  That gives us a file with a single line that looks like this:  
  
  ```
  [{"name": "Sabrina Green", "username": "sgreen", "phone": {"office": "802-867-5309", "cell": "802-867-5310"}, "department": "IT Infrastructure", "role": "Systems Administrator"}, {"name": "Eli Jones", "username": "ejones", "phone": {"office": "684-348-1127"}, "department": "IT Infrastructure", "role": "IT Specialist"}]
  ```
- JSON doesn't need to contain multiple lines, but it sure can be hard to read the result if it's formatted this way! Let's use the indent parameter for json.dump() to make it a bit easier to read.  
  
  ```python
  with open('people.json', 'w') as people_json:
      json.dump(people, people_json, indent=2)
  ```
  The resulting file should look like this:

  ```json
  [
    {
      "name": "Sabrina Green",
      "username": "sgreen",
      "phone": {
        "office": "802-867-5309",
        "cell": "802-867-5310"
      },
      "department": "IT Infrastructure",
      "role": "Systems Administrator"
    },
    {
      "name": "Eli Jones",
      "username": "ejones",
      "phone": {
        "office": "684-348-1127"
      },
      "department": "IT Infrastructure",
      "role": "IT Specialist"
    }
  ]
  ```
- Another option is to use the dumps() method, which also serializes Python objects, but returns a string instead of writing directly to a file.
  
  ```bash
  >>> import json
  >>> 
  >>> people = [
  ...   {
  ...     "name": "Sabrina Green",
  ...     "username": "sgreen",
  ...     "phone": {
  ...       "office": "802-867-5309",
  ...       "cell": "802-867-5310"
  ...     },
  ...     "department": "IT Infrastructure",
  ...     "role": "Systems Administrator"
  ...   },
  ...   {
  ...     "name": "Eli Jones",
  ...     "username": "ejones",
  ...     "phone": {
  ...       "office": "684-348-1127"
  ...     },
  ...     "department": "IT Infrastructure",
  ...     "role": "IT Specialist"
  ...   }
  ... ]
  >>> people_json = json.dumps(people)
  >>> print(people_json)
  [{"name": "Sabrina Green", "username": "sgreen", "phone": {"office": "802-867-5309", "cell": "802-867-5310"}, "department": "IT Infrastructure", "role": "Systems Administrator"}, {"name": "Eli Jones", "username": "ejones", "phone": {"office": "684-348-1127"}, "department": "IT Infrastructure", "role": "IT Specialist"}]
  ```
- The load() method does the inverse of the dump() method. It deserializes JSON from a file into basic Python objects. The loads() method also deserializes JSON into basic Python objects, but parses a string instead of a file.  

  ```bash
  >>> import json
  >>> with open('people.json', 'r') as people_json:
  ...     people = json.load(people_json)
  ... 
  >>> print(people)
  [{'name': 'Sabrina Green', 'username': 'sgreen', 'phone': {'office': '802-867-5309', 'cell': '802-867-5310'}, 'department': 'IT Infrastructure', 'role': 'Systems Administrator'}, {'name': 'Eli Jones', 'username': 'ejones', 'phone': {'office': '684-348-1127'}, 'department': 'IT Infrastructure', 'role': 'IT Specialist'}, {'name': 'Melody Daniels', 'username': 'mdaniels', 'phone': {'cell': '846-687-7436'}, 'department': 'User Experience Research', 'role': 'Programmer'}, {'name': 'Charlie Rivera', 'username': 'riverac', 'phone': {'office': '698-746-3357'}, 'department': 'Development', 'role': 'Web Developer'}]
  ```

## The Python Requests Library
- When you visit a webpage with your web browser, the browser is making a series of HTTP requests to web servers somewhere out on the Internet. Those servers will answer with HTTP responses. This is also how we’re going to send and receive messages with web applications from our code.
- The Python Requests library makes it super easy to write programs that send and receive HTTP. Instead of having to understand the HTTP protocol in great detail, you can just make very simple HTTP connections using Python objects, and then send and receive messages using the methods of those objects. Let's look at an example:  

  ```bash
  >>> import requests
  >>> response = requests.get('https://www.google.com')
  ```
  That was a basic request for a web page! We used the Requests library to make a HTTP GET request for a specific URL, or Uniform Resource Locator. First 300 characters of response.text:
  
  ```bash
  >>> print(response.text[:300])
  <!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="de"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="dZfbIAn803LDGXS9
  ```
  Not that HTML can't be messy enough on its own, but let's look at the first bytes of the raw message that we received from the server:  

  ```bash
  >>> response = requests.get('https://www.google.com', stream=True)
  >>> print(response.raw.read()[:100])
  b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x02\xff\xc5Z\xdbz\x9b\xc8\x96\xbe\xcfS`\xf2\xb5-\xc6X\x02$t\xc28\xe3v\xdc\xdd\xee\xce\xa9\xb7\xdd;\xe9\x9d\xce\xf6W@\t\x88\x11`@>D\xd6\x9b\xce\xe5<\xc3\\\xcd\xc5\xfc\xab8\x08\xc9Nz\x1f.&\x8e1U\xb5j\xd5:\xfc\xb5jU\x15\x87;^\xe2\x16\xf7)\x97\x82b\x1e\x1d\x1d\xd2S'
  ```
  The response was compressed with gzip, so it had to be decompressed before we could even read the text of the HTML. The requests.Response object also contains the exact request that was created for us. We can check out the headers stored in our object to see that the Requests module told the web server that it was okay to compress the content:  

  ```bash
  >>> response.request.headers['Accept-Encoding']
  'gzip, deflate'
  ```
  And then the server told us that the content had actually been compressed.  

  ```bash
  >>> response.headers['Content-Encoding']
  'gzip'
  ```
  
## Useful Operations for Python Requests
- You can check out the value of Response.ok, which will be True if the response was good, and False if it wasn't.  

  ```bash
  >>> response.ok
  True
  ```
- You can get the HTTP response code that was returned by looking at Response.status_code:  

  ```bash
  >>> response.status_code
  200
  ```
- To write maintainable, stable code, you’ll always want to check your responses to make sure they succeeded before trying to process them further. For example, you could do something like this:  

  ```python
  response = requests.get(url)
  if not response.ok:
      raise Exception("GET failed with status code {}".format(response.status_code))
  ```
- We can use the Response.raise_for_status() method, which will raise an HTTPError exception only if the response wasn’t successful.  

  ```python
  response = requests.get(url)
  response.raise_for_status()
  ```
- With requests.get(), you can provide a dictionary of parameters, and the Requests module will construct the correct URL for you! 

  ```bash
  >>> p = {"search": "grey kitten",
  ...      "max_results": 15}
  >>> response = requests.get("https://example.com/path/to/api", params=p)
  >>> response.request.url
  'https://example.com/path/to/api?search=grey+kitten&max_results=15'
  ```
  Query strings are handy when we want to send small bits of information, but as our data becomes more complex, it can get hard to represent it using query strings. 
  
- In our scripts, a POST request looks very similar to a GET request. Instead of setting the params attribute, which gets turned into a query string and appended to the URL, we use the data attribute, which contains the data that will be sent as part of the POST request.  

  ```bash
  >>> p = {"description": "white kitten",
  ...      "name": "Snowball",
  ...      "age_months": 6}
  >>> response = requests.post("https://example.com/path/to/api", data=p)
  ```
  Response:
  
  ```bash
  >>> response.request.url
  'https://example.com/path/to/api'

  >>> response.request.body
  'description=white+kitten&name=Snowball&age_months=6'
  ```
- So, if we need to send and receive data from a web service, we can turn our data into dictionaries and then pass that as the data attribute of a POST request. Today, it's super common to send and receive data specifically in JSON format, so the Requests module can do the conversion directly for us, using the json parameter.  

  ```bash
  >>> response = requests.post("https://example.com/path/to/api", json=p)
  >>> response.request.url
  'https://example.com/path/to/api'
  >>> response.request.body
  b'{"description": "white kitten", "name": "Snowball", "age_months": 6}' 
  ```
  
## What is Django?
- Django is a full-stack web framework written in Python.
- A full-stack web framework handles a bunch of different components that are typical when creating a web application. It contains libraries that help you handle each of the pieces: writing your application's code, storing and retrieving data, receiving web requests, and responding to them. 
- Web frameworks are commonly split into three basic components: (1) the application code, where you'll add all of your application's logic; (2) the data storage, where you'll configure what data you want to store and how you're storing it; and (3) the web server, where you'll state which pages are served by which logic.
- Django has a ton of useful components for building websites. In the lab project, Django will be used for serving the company website, including customer reviews. It does this by taking the request for a URL and parsing it using the urlresolver module. This is a core module in Django that interprets URL requests and matches them against a list of defined patterns. If a URL matches a pattern, the request is passed to the associated function, called a view. This allows you to serve different pages depending on what URL is being requested. You can even build complex logic into the function handling the request to make more dynamic, interactive, and exciting pages.
- Django can also handle reading and writing data from a database, letting you store and retrieve data used by your application. In the lab, the database holds the customer reviews for the company. When a user loads the website, the logic will ask the database for all available customer reviews. These are retrieved and formatted into a web page, which is served as a response to the URL request. Django makes it easy to interact with data stored in a database by using an object-relational mapper, or ORM. This tool provides an easy mapping between data models defined as Python classes and an underlying database that stores the data in question.
- On top of this, the Django application running in the lab includes an endpoint that can be used to add new customer reviews to the database. This endpoint is configured to receive data in JSON format, sent through an HTTP POST request. The data transmitted will then be stored in the database and added to the list of all reviews. The framework even generates an interactive web form, that lets us directly interact with the endpoint using our browser, which can be really handy for testing and debugging.

