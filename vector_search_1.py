#NOT USING

#creating client
from vector_search_all import *

# new code

docsearch = Typesense.from_documents(
    docs,
    embeddings,
    typesense_client_params={
        "host": "127.0.0.1",  # Use xxx.a1.typesense.net for Typesense Cloud
        "port": "8108",  # Use 443 for Typesense Cloud
        "protocol": "http",  # Use https for Typesense Cloud
        "typesense_api_key": "xyz",
        "typesense_collection_name": "lang-chain",
    },
)