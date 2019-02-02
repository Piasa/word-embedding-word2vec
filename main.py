import json
from pprint import pprint

file = "/Users/gaoyifan/Downloads/CVDataset/cvDataset.json"
fb = open(file, 'r')
load_dict = json.load(fb)
fb.close()
pprint(load_dict)
