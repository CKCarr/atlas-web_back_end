""" # 8. List all documents in Python

Write a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
"""
from typing import List

def list_all(mongo_collection: object) -> list:
    """  list all documents in a collection """
