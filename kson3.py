import logging
from typing import Any
import json
from json import JSONEncoder

# First set up a logger to use logging instead of printing
logging.basicConfig(level=logging.INFO, format='%(message)s')

# define a user class to be used to encode the json file
class User:
  def __init__(self, name, age):
    self.name = name 
    self.age = age
    
user = User('Mvano', 10)

# write a custom encoding function which check whether an object in an instance of a given class and returns a dictionary with the keys as instance variables.
def encode_user(object):
  if isinstance(object, User):
    return {
      'name': object.name, 'age': object.age, object.__class__.__name__: True
      }
  else:
    raise TypeError('object of type user is not JSON serializable or convertable')

# then dump the user object into the json file
userJSON = json.dumps(user, default=encode_user)

logging.info(f"\n{userJSON}")

# alternatively a custom encoding function can be defined suhc that it's contained inside a class:

class UserEncoder(JSONEncoder):
  def default(self, object):
    if isinstance(object, User):
      return {
        'name': object.name, 'age': object.age, object.__class__.__name__: True
        }
    else:
      return JSONEncoder.default(self, object)
    
userJSON = json.dumps(user, cls=UserEncoder)

logging.info(f"\n{userJSON}")

# the above user encoder class can also be used directly 
userJSON = UserEncoder().encode(user)

logging.info(f"\n{userJSON}")

# the encoded json file can be decoded back to python a dictionary 
user = json.loads(userJSON)

logging.info(f"\n{user}")

# the encoded json file can also be converted to a python object by first defining a decoding user function:
def decode_user(dictionary):
  if User.__name__ in dictionary:
    return User(name = dictionary['name'], age=dictionary['age'])
  
  else:
    return dictionary
  
# use the decodeing user function
user = json.loads(userJSON, object_hook=decode_user)

logging.info(f"\n{user.name}")