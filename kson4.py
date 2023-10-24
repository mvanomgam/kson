import logging

# First set up a logger to use logging instead of printing
logging.basicConfig(level=logging.INFO, format='%(message)s')

import json

# load the json file to a python object 
with open("states.json") as file:
  data = json.load(file)

for state in data['states']:
  logging.info(f"\n{state['name']} {state['abbreviation']}")
  
# load or write the python object to a json file 

# first remove are codes in this example:
for state in data['states']:
  del state['area_codes']
  
# then write the file as json
with open("new_states.json", "w") as file:
  json.dump(data, file, indent=2)
  

  
