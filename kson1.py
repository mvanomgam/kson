import logging

# First set up a logger to use logging instead of printing
logging.basicConfig(level=logging.INFO, format='%(message)s')

# JSON - JavaScript Object Notation
# used for data exchange and heavily used in web applications

# relationship between python and JSON is shown below:

# Python          JSON
# dict            object
# list, tuple     array
# str             string
# int, float      number
# True            true
# False           false
# None            null

################################################################

# import the JSON module
import json

# 1. converting a python dictionary to a json object

person = {
  "name": "mvano",
  "age": 30,
  "city": "cape town",
  "hasChildren": False,
  "titles": ["actuarial analyst", "programmer"]
}

# dumb the string dictionary to json object
personJSON = json.dumps(person, indent=4, sort_keys=True)

# finally log or print the json object
logging.info(f"\n{personJSON}")

# 2. converting json object to a python object
# load the json string to convert it to a python object
person = json.loads(personJSON)

# finally print or log the python object
logging.info(f"\n{person}")

################################################################

# 1. Load or dumb the disctionary data to a json file by:
# open a file in writing mode so that a file can be created if it does not exist.
# then dumping the person dictionary to the person.json file
with open('person.json', 'w') as file:
  json.dump(person, file, indent=4)
  
# 2. convert json file to a python object by:
# open a json file in read mode because it already exist.
# then load the json data to convert it to python format.
with open('person.json', 'r') as file:
  person = json.load(file)
  logging.info(f"\n{person}")