import json

with open("large-file.json","r", encoding="utf-8") as file:
    data = json.load(file)

for record in data:
    if "size" in record:
        record["size"] = 42

data.reverse()

with open("output.2.3.json", "w", encoding="utf-8") as out:
    json.dump(data, out, indent=4)