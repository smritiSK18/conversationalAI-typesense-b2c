import typesense
from typesense_client2 import *

#funtion testing semantic function
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
