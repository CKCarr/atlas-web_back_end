#!/usr/bin/env python3
""" # 8. List all documents in Python

Write a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
"""
from typing import List
from pymongo.collection import Collection

def list_all(mongo_collection: Collection) -> List:
    """  list all documents in a collection
    args: mongo_collection: pymongo collection object
    """
    documents = []
    for doc in mongo_collection.find():
        documents.append(doc)
    return documents
