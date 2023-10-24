import logging

# First set up a logger to use logging instead of printing
logging.basicConfig(level=logging.INFO, format='%(message)s')

class User:
  def __init__(self, name, age):
    self.name = name 
    self.age = age
    
user = User('Mvano', 10)

# convert this to a json
import json

# first write a custom encoding function which check whether an object in an instance of a given class and returns a dictionary with the keys as instance variables.
def encode_user(object):
  if isinstance(object, User):
    return {
      'name': object.name, 'age': object.age, object.__class__.__name__: True
      }
  else:
    raise TypeError('object of type user is not JSON serializable or convertable')
  
userJSON = json.dumps(user, default=encode_user)

logging.info(f"\n{userJSON}")