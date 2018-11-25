import json
with open("characters.json", "w") as write_file:
    json.dump(data, write_file)