import logging
import json

##################################################################

# First set up a logger to use logging instead of printing:

# if this logger does not exist then it will be created.
logger = logging.getLogger(__name__)

# set the log level on the logger
logger.setLevel(logging.DEBUG)

# create a formatter for the logger
formatter = logging.Formatter('%(message)s ')

# create a file handler to specify the file that will be logged to.
file_handler = logging.FileHandler('jsonLog.log')

# add the formatter to the file handler and set the level to be logged to the log file.
# i this case this means the debug statements will not be logged.
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# add the file handler to the logger 
logger.addHandler(file_handler)

# debug statements can be displayed on the console by setting up stream handler
stream_handler = logging.StreamHandler()

# add the formatter to the stream handler
stream_handler.setFormatter(formatter)

# add the stream handler to the logger
logger.addHandler(stream_handler)

##################################################################

# 1. Write a Dictionary to a JSON File - Dictionary Object to JSON

dog = {
  "Name": "Rover",
  "Breed": "Pug",
  "Age": 5,
  "Owners": [
    {
      "Name": "Mvano",
      "Age": 25
    },
    {
      "Name": "Cecilia",
      "Age": 30
    }
  ]
}

# create a json file using the writing mode
with open('dog.json', 'w') as file:
  json.dump(dog, file, indent=2)

##################################################################

# 2. Read a JSON File to a Dictionary 
# create an empty dictionary
data = {}

# open the json file using the reading mode
with open('dog.json', 'r') as file:
  data = json.load(file)

# add another dog by first creating dog list containg a dictionary for each dog.

dogs = [{}, {}]

dogs[0].update(Name='Golder', Breed='Bulldog', Age=1)
dogs[1].update(Name=data['Name'], Breed=data['Breed'], Age=data['Age'])

# create animals dictionary to contain the dogs and owners
animals = {}
animals.update(Dogs=dogs, Owners=data['Owners'])

# Write the animals dictionary to a JSON File

with open('animals.json', 'w') as file:
  json.dump(animals, file, indent=2)

##################################################################

# 3. Parse JSON in Python 
# import the requests module to parse the data
import requests

# Use requests to fecth the data and store it on a variable
response = requests.get('https://dummyjson.com/products')

# convert the request variable to a python dictionary
responseDict = response.json()

# check if it's indeed a python dictionary
logger.info(f"\n{type(responseDict)}")

# write the original dictionary to a JSON 
with open('originalProducts.json', 'w') as file:
  json.dump(responseDict, file, indent=2)
  
# delete the thumbnail and images
for i in range(len(responseDict['products'])):
  del responseDict['products'][i]['thumbnail']
  del responseDict['products'][i]['images']

# write the dictionary to a JSON 
with open('newProducts.json', 'w') as file:
  json.dump(responseDict, file, indent=2)