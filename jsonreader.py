import json
from pprint import pprint

with open("C:\cygwin64\home\Premkumar.Nagarajan\Lineage") as data_file:
    data = json.load(data_file)

k=data['result']

for  i in  k:
    print i['name']

