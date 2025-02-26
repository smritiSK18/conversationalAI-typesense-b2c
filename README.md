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
1. ** Python Client (`python_client.py`) **-creating a python client to typesense server in local
3. ** Collection Schema (`collection_schema.py`) **- definig the schema of our collection. Manually done since the dataset had duplicate column headings
4. ** Creating collection(`create_collection.py`) **- creating a collection object of any existing schema
5. ** Dataset (`diagnostic_dataset_new.json`) **- dataset contiaing all test data
6. ** Uploading data(`document_upload.py`) **- uploading dataset data to collection object
7. ** List of queries (`query_list.py`) **- list of templates of query definitions
8. ** Calling quer(`call_query.py`) **- calling queries from the query_list.py
9. **(`additional`) **- rarely required fuctions
      1. **(`py_delete_schema.py`) **- to delete any schema
 

