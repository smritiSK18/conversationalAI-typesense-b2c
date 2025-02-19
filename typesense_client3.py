#NOT USING

import typesense

# Step 1: Initialize the Typesense client
client = typesense.Client({
    'nodes': [{
        'host': '127.0.0.1',  # Your Typesense host
        'port': '8108',       # Your Typesense port
        'protocol': 'http'    # Or 'https' if you're using SSL
    }],
    'api_key': 'xyz',  # Your Typesense API key
    'connection_timeout_seconds': 2
})

# Step 2: Create a collection schema
collection_schema = {
    'name': 'products',
    'fields': [
        {'name': 'id', 'type': 'string'},
        {'name': 'name', 'type': 'string'},
        {'name': 'price', 'type': 'float'},
        {'name': 'category', 'type': 'string'},
        {
            "name": "embedding",
            "type": "float[]",
            "embed": {
              "from": [
                "product_name"
              ],
              "model_config": {
                "model_name": "ts/all-MiniLM-L12-v2"
              }
            }
        }
    ],
    'default_sorting_field': 'price'
}

# Create the collection
client.collections.create(collection_schema)

# Step 3: Add documents to the collection
documents = [
    {'id': '1', 'name': 'Product 1', 'price': 100.0, 'category': 'electronics'},
    {'id': '2', 'name': 'Product 2', 'price': 150.0, 'category': 'furniture'},
    {'id': '3', 'name': 'Product 3', 'price': 80.0, 'category': 'electronics'},
    {'id': '4', 'name': 'Product 4', 'price': 10.0, 'category': 'electronics'},
    {'id': '5', 'name': 'Product 5', 'price': 15.0, 'category': 'furniture'},
    {'id': '6', 'name': 'Product 6', 'price': 80.0, 'category': 'electronics'},
    {'id': '7', 'name': 'Product 7', 'price': 190.0, 'category': 'electronics'},
    {'id': '8', 'name': 'Product 8', 'price': 170.0, 'category': 'furniture'},
    {'id': '9', 'name': 'Product 9', 'price': 60.0, 'category': 'electronics'},
]





print('/////')
print('PRINTING DATA IN COLLECTION')

try:
    response = client.collections['products'].documents.import_(documents)
    print("Document import response:", response)
except Exception as e:
    print("Error importing documents:", e)


print('/////')

print('QUERY RESULT')




try:  
    results = client.collections['your_collection_name'].documents.search({
    'q': 'furniture',  # The search term
    'query_by': 'id,name,price',
    'filter_by': 'price: [10 TO 100]'  # Filtering results based on price range
})
  
    print("Search results (all documents):")
    for hit in results['hits']:
        print(hit['document'])  # Print each matching document
except Exception as e:
    print("Error searching:", e)
