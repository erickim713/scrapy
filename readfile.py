import json
from pprint import pprint

with open('quotes.json') as data_file:
    data = json.load(data_file)
print(data[0]['company-name'])
