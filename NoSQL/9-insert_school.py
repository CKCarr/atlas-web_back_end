#!/usr/bin/env python3
""" 9. Insert a document in Python
Write a Python function that inserts a new document in a collection based on kwargs:

Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id

"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection based on kwargs.

    :param mongo_collection: The PyMongo collection object
    :param kwargs: The key-value pairs to be inserted as a document
    :return: The new _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
