
from typesense_client2 import client
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

# Function to perform fuzzy search (not an exact match) - through 'num typos' field
def fuzzy_search():
    try:
        results = client.collections['products'].documents.search({
            'q': 'Product',
            'query_by': 'name',
            'num_typos': 3 
        })
        print("*** Fuzzy Search Results:")
        for hit in results['hits']:
            print(hit['document'])
    except Exception as e:
        print("Error in fuzzy_search:", e)


# Add more query functions as needed
def test_query(): 
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


# Semantic search
def semantic_search():
    try:
        response = client.multi_search.perform(
            search_queries={
                "searches": [
                    {
                        "q":"Coomb's test",
                        "query_by": "Tests,1 line description (20-30 words description),Alias (2-3) - Other name,Risk assessment (3-4)\n\nWhat problems is it taken for?,embedding",
                        "collection": "products",
                        "prefix": "false",
                        "vector_query": "embedding:([], k: 200)",
                        "exclude_fields": "embedding",
                        "per_page": 3
                    }
                ]
            },
            common_params={}
        )
        print("Multi-Search Response:", response)
    except Exception as e:
        print("Error performing multi-search:", e)
