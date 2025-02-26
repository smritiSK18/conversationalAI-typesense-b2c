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
1. __ Python Client (`python_client.py`) __-creating a python client to typesense server in local
3. __ Collection Schema (`collection_schema.py`) __- definig the schema of our collection. Manually done since the dataset had duplicate column headings
4. __ Creating collection(`create_collection.py`) __- creating a collection object of any existing schema
5. __ Dataset (`diagnostic_dataset_new.json`) __- dataset contiaing all test data
6. __ Uploading data(`document_upload.py`) __- uploading dataset data to collection object
7. __ List of queries (`query_list.py`) __- list of templates of query definitions
8. __ Calling quer(`call_query.py`) __- calling queries from the query_list.py
9. __(`additional`) __- rarely required fuctions
      1. __(`py_delete_schema.py`) __- to delete any schema
 

