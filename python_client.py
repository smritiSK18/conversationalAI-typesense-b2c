import typesense

# Initialize the Typesense client
client = typesense.Client({
    'nodes': [{
        'host': '127.0.0.1',  # Your Typesense host
        'port': '8108',       # Your Typesense port
        'protocol': 'http'    # Or 'https' if you're using SSL
    }],
    'api_key': 'xyz',  # Your Typesense API key
    'connection_timeout_seconds': 30
})
