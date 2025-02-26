# ai-typesense-b2c
Conversational AI for B2C product search using Typesense


## Overview :
* python client
* data in - JSON file
* can adjust priority of - keyword search, semantic search 
* has feature to add - filters
* conversion to embeddings using “all-MiniLM-L12-v2” - transformer based sentence embedding model
<br/>


## Components :

1. **Python Client (`python_client.py`)** -creating a python client to typesense server in local
2. **Collection Schema (`collection_schema.py`)** - definig the schema of our collection. Manually done since the dataset had duplicate column headings
3. **Creating collection(`create_collection.py`)** - creating a collection object of any existing schema
4. **Dataset (`diagnostic_dataset_new.json`)** - dataset contiaing all test data
5. **Uploading data(`document_upload.py`)** - uploading dataset data to collection object
6. **List of queries (`query_list.py`)** - list of templates of query definitions
7. **Calling quer(`call_query.py`)** - calling queries from the query_list.py
8. **Additional functions(`additional`)** - rarely required fuctions
      1. **Delete schema(`py_delete_schema.py`)** - to delete any schema
      2. **Collection Schema creation(`collection_schema_creation.py`)** - to automatically create schema from dataset(JSON) file
 




