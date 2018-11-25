import json

with open('characters.json', 'r') as f:
    json_text = f.read()

# Decode the JSON string into a Python dictionary.
apod_dict = json.loads(json_text)
print(apod_dict['essai'])

# Encode the Python dictionary into a JSON string.
#new_json_string = json.dumps(apod_dict, indent=4)
#print(new_json_string)