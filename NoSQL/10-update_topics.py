#!/usr/bin/env python3
""" 10. Change school topics

Write a Python function that changes all topics of a school document based on the name:

Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name (string) will be the school name to update
topics (list of strings) will be the list of topics approached in the school
"""



def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the school name.

    :param mongo_collection: The PyMongo collection object.
    :param name: The name of the school to update.
    :param topics: The list of topics approached in the school.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
