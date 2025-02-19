import typesense
from typesense_client2 import *
import json

# Documents to import
'''
documents = [
    {'id': '1', 'name': 'coumb', 'price': 100.0, 'category': 'electronics'},
    {'id': '2', 'name': 'hair brush', 'price': 150.0, 'category': 'furniture'},
    {'id': '3', 'name': 'pan', 'price': 80.0, 'category': 'electronics'},
]
'''
'''
try:
    with open('/Users/smriti.kashyap/work-project-1/python_client_(child0)/pj_dataset.json', 'r') as file:
        documents = json.load(file) 

    response = client.collections['test_info'].documents.import_(document1)
    print("Import Response:", response)
except Exception as e:
    print("Error importing documents:", e)


# Import documents
try:

    response = client.collections['products'].documents.import_(documents)
    print("Import Response:", response)
except Exception as e:
    print("Error importing documents:", e)
'''

try:
    with open('/Users/smriti.kashyap/work-project-1/python_client_(child0)/pj_dataset_new.json', 'r') as file:
        documents = json.load(file) 

    for doc in documents:
        for field in ['Date', 'Date_2', 'Date_5','']:
            if field in doc:
                doc[field] = str(doc[field])
        
    response = client.collections['products'].documents.import_(documents)
    print("Import Response:", response)
except Exception as e:
    print("Error importing documents:", e)