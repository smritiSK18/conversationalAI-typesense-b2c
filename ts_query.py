#NOT USING

# 1-4 query - works
from typesense_client2 import client
#from document import response
#from ss_documents import *
import typesense

# Function to search all documents
def search_all():
    try:
        results = client.collections['products'].documents.search({
            'q': '*',
            'query_by': 'name'
        })
        print("*** All Documents:")
        for hit in results['hits']:
            print(hit['document'])
    except Exception as e:
        print("Error in search_all:", e)


#print('/////////')
# Function to filter documents
def search_with_filter():
    try:
        results = client.collections['products'].documents.search({
            'q': '*',
            'query_by': 'name',
            'filter_by': 'category:electronics && price:<150'
        })
        print("*** Filtered Documents:")
        for hit in results['hits']:
            print(hit['document'])
    except Exception as e:
        print("Error in search_with_filter:", e)

# Function to perform fuzzy search
def fuzzy_search():
    try:
        results = client.collections['products'].documents.search({
            'q': 'Product',
            'query_by': 'name',
            'num_typos': 0  #didn't find where it is stored/specified?, also works for all
        })
        print("*** Fuzzy Search Results:")
        for hit in results['hits']:
            print(hit['document'])
    except Exception as e:
        print("Error in fuzzy_search:", e)

# Add more query functions as needed
def child_query(): 
    try:
        # Search for all documents
        results = client.collections['products'].documents.search({
            'q': 'Product',  # Use '*' to match all documents
            'query_by': 'name',  # Specify the field to query against
            'filter_by': 'price:150.0'
        })
        print("Search results (all documents):")
        for hit in results['hits']:
            print(hit['document'])  # Print each matching document
    except Exception as e:
        print("Error searching:", e)
