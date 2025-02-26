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

1. **Python Client (`python_client.py`)**
   Creating a python client to typesense server in local
   
3. **Collection Schema (`collection_schema.py`)**
    Definig the schema of our collection. Manually done since the dataset had duplicate column headings
   
5. **Creating collection(`create_collection.py`)**
    Creating a collection object of any existing schema
   
7. **Dataset (`diagnostic_dataset_new.json`)**
    Dataset contiaing all test data
   
9. **Uploading data(`document_upload.py`)**
     Uploading dataset data to collection object
   
11. **List of queries (`query_list.py`)**
     List of templates of query definitions
    
13. **Calling quer(`call_query.py`)**
     Calling queries from the query_list.py
    
15. **Additional functions(`additional`)**
     Rarely required fuctions

      1. **Delete schema(`py_delete_schema.py`)**
          To delete any existing schema
      3. **Collection Schema creation(`collection_schema_creation.py`)**
          To automatically create schema from dataset(JSON) file
 




