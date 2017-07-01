import json
from pprint import pprint

with open('quotes.json') as data_file:
    data = json.load(data_file)

for entry in data:
    print("회사:" + entry['company-name'])
    print("설명:" + entry['description'])
