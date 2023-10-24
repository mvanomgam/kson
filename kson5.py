import logging

# First set up a logger to use logging instead of printing
logging.basicConfig(level=logging.INFO, format='%(message)s')

import json
from urllib.request import urlopen

# get the latest currency data using an API by:
with urlopen("http://data.fixer.io/api/latest?access_key=39dfcdf2b81ded813143a7ce2074c76e&symbols") as response:
  source = response.read()

# load this to a python object
data = json.loads(source)

# dumb the currency data to a json file
with open('currencyData.json', 'w') as file:
  json.dump(data, file, indent=2)

# dumb the data back to a json string and apply indentation 
dataJSON = json.dumps(data, indent=2)

# separate currencies to stronger currencies (<= 2) and weak currencies 

# open the json file as a dictionary in python
with open('currencyData.json', 'r') as file:
  currencyData = json.load(file)
  
strongCurrencies = {}
weakCurrencies = {}

for symbol in currencyData["rates"].keys():
  if symbol not in strongCurrencies:
    if currencyData["rates"][str(symbol)] <= 2:
      strongCurrencies[str(symbol)] = currencyData["rates"][str(symbol)]
    else:
      weakCurrencies[str(symbol)] = currencyData["rates"][str(symbol)]
      
# dumb both strong and weak currency data to a json file
with open('strongCurrencies.json', 'w') as file:
  json.dump(strongCurrencies, file, indent=2)

with open('weakCurrencies.json', 'w') as file:
  json.dump(weakCurrencies, file, indent=2)
  
# logging.info(f"{rates}")

# print or log the data
# logging.info(dataJSON)