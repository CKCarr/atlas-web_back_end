#!/usr/bin/env python3
""" 11. Where can I learn Python?
Write a Python function that returns the list of school having a specific topic:

Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection will be the pymongo collection object
topic (string) will be topic searched
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools from the collection that have a specific topic.

    :param mongo_collection: The PyMongo collection object.
    :param topic: The topic being searched for.
    :return: A list of dictionaries representing the schools that have the specified topic.
    """
    # Query the collection for schools with the specified topic
    schools = mongo_collection.find({"topics": topic})
    # Convert the cursor to a list of dictionaries and return it
    return list(schools)
