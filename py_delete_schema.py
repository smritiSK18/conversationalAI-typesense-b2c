import typesense
from typesense_client2 import *

def my_delete_schema():

    collection_name = "products"

    try:
        client.collections["products"].delete()
        print(f"Collection '{"products"}' deleted successfully.")
    except typesense.exceptions.ObjectNotFound:
        print(f"Collection '{"products"}' does not exist.")


#def delete_collections():
def py_retrieve():
    try:
        # Replace '1' with the ID of the document you want to print
        document = client.collections['products'].documents['7'].retrieve()
        print("Document:", document)
    except Exception as e:
        print("Error retrieving document:", e)