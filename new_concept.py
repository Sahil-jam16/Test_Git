import json

def extract_values(json_data):
    values = []
    if isinstance(json_data, dict):
        for value in json_data.values():
            values.extend(extract_values(value))
    elif isinstance(json_data, list):
        for item in json_data:
            values.extend(extract_values(item))
    else:
        values.append(json_data)
    return values

# Replace 'path/to/json/file.json' with the actual path to your JSON file
json_file_path = 'path/to/json/file.json'

with open(json_file_path) as file:
    json_data = json.load(file)

all_values = extract_values(json_data)
print(all_values)
