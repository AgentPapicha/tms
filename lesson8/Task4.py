import json
import pandas as pd

with open("data_file.json") as read_file:
   pyson = json.load(read_file)
print(pyson)

df = pd.read_json(pyson)
df.to_csv('file.csv')
