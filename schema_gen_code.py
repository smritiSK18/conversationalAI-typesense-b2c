#NOT USING this - as schema is not accurate // won't allow duplicate col titles - eg. name, date

import json

# Load the schema from the JSON file
with open('pj_dataset_new.json', 'r') as file:
    schema = json.load(file)

# Print the schema in a readable format

print(json.dumps(schema, indent=4))