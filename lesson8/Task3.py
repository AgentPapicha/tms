import json
new_dict = {
    "012024": ('Alex', 24),
    "012028": ('Sonia', 28),
    "012047": ('Egor', 47),
    "012033": ('Fedor', 33),
    "012026": ('Rita', 26),
}

data = new_dict
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
    