#1- open vm
#   *   source work-project-1/venv/bin/activate
#2-  goto directory(root)
#3-  create - client, schema, data doc, import data doc, query list, query calls
#4- delete collection
'''    curl -X DELETE http://localhost:8108/collections/products \
  -H "X-TYPESENSE-API-KEY:xyz"

'''

#5- query(terminal)
'''
curl 'http://localhost:8108/multi_search' \
    -H "X-TYPESENSE-API-KEY: xyz" \
    -X POST \
    -d '{
      "searches": [
        {
          "q": "lipids",
          "query_by": "embedding",
          "collection": "products",
          "prefix": "false",
          "exclude_fields": "embedding",
          "per_page": 1
        }
      ]
    }
'''




# -- products created with embed ==> [done]
