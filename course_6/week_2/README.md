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
