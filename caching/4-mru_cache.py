#!/usr/bin/python3
""" 4. MRU Caching
Create a class MRUCache that inherits
from BaseCaching and is a caching system:

You must use self.cache_data -
dictionary from the parent class BaseCaching
You can overload def __init__(self):
but don’t forget to call the parent init: super().__init__()

def put(self, key, item):
    Must assign to the dictionary self.cache_data
    the item value for the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data
    is higher that BaseCaching.MAX_ITEMS:
    you must discard the most recently used item (MRU algorithm)
    you must print DISCARD:
    with the key discarded and following by a new line
def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data,
    return None.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU cache system takes the last element in
        and pops that last element out
        when Max cap is reached

    Args:
        BaseCaching ( class ): Parent class
    """
    def __init__(self):
        """ Initialize class instance to empty
        to create new instance of MRU cache system
        """
        super().__init__()
        self.key_order_tracker = []
# end of init method

    def put(self, key, item):
        """ Add key/value pairs to the cache system using MRU """
        # do this if key and item are not None
        if key is not None and item is not None:
            # do this if key is in cache
            if key in self.cache_data:
                # remove key from tracker
                self.key_order_tracker.remove(key)
            # do this if cache is at max capacity
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # remove last key in tracker
                last_key = self.key_order_tracker.pop()
                # remove last key from cache
                del self.cache_data[last_key]
                # print message
                print("DISCARD: {}".format(last_key))
            # add key to tracker
            self.key_order_tracker.append(key)
            # add key and item to cache
            self.cache_data[key] = item
# end of put method

    def get(self, key):
        """ Get value from cache using key """
        # do this if key is not None and key is in cache
        if key is not None and key in self.cache_data:
            # remove key from tracker
            self.key_order_tracker.remove(key)
            # add key to tracker
            self.key_order_tracker.append(key)
            # return value of key
            return self.cache_data[key]
        return None
# end of get method
