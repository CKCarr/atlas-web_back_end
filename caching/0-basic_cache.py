#!/usr/bin/python3
""" 0. Basic dictionary

Create a class BasicCache that inherits from BaseCaching
and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit

def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.

def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from  import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class that inherits from  BaseCaching and is a caching system.

    Args:
        BaseCaching (class): BaseCaching class to inherit from

    Functions: (methods defined here)
        put: method that adds an item to the cache. If the key or the item is non the method does nothing.
        get: method that gets an item from the cache by it's key. If the key is 'None' or doesn't exist in the cache, it returns 'None'.
    """
    
    def put(self, key, item):
        """ put method - adds an item to the cache.
        must assign to the dictionary self.cache_data

        Args:
            key (): _description_
            item (_type_): _description_
        """
