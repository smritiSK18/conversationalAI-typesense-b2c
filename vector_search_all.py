#NOT USING


import typesense

#/////////////---1

import getpass
import os

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

#/////////////---2

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Typesense
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter


#/////////////---3
from langchain.embeddings.openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(openai_api_key="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")


#/////////////---4
from langchain.document_loaders import TextLoader

from langchain.document_loaders import JSONLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings

loader = TextLoader("/Users/smriti.kashyap/work-project-1/python_client_(child0)/pj_dataset_new.json")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

#/////////////---3

#/////////////---5

#/////////////---6
#pip install --upgrade --quiet  typesense openapi-schema-pydantic langchain-openai langchain-community tiktoken

import getpass
import os

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Typesense
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

loader = TextLoader("../../how_to/state_of_the_union.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

docsearch = Typesense.from_documents(
    docs,
    embeddings,
    typesense_client_params={
        "host": "localhost",  # Use xxx.a1.typesense.net for Typesense Cloud
        "port": "8108",  # Use 443 for Typesense Cloud
        "protocol": "http",  # Use https for Typesense Cloud
        "typesense_api_key": "xyz",
        "typesense_collection_name": "lang-chain",
    },
)

query = "What did the president say about Ketanji Brown Jackson"
found_docs = docsearch.similarity_search(query)

print(found_docs[0].page_content)


#retriever
retriever = docsearch.as_retriever()
retriever

query = "What did the president say about Ketanji Brown Jackson"
retriever.invoke(query)[0]