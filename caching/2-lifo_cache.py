#!/usr/bin/python3
""" 2. LIFO Caching

Create a class LIFOCache that inherits from BaseCaching
and is a caching system:

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
    you must discard the last item put in cache (LIFO algorithm)
    you must print DISCARD: with the key discarded
    followed by a new line

def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data,
    return None.
"""

# BaseCaching = __import__('base_caching').BaseCaching

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache system takes the last element in
        and pops that last element out
        when Max cap is reached

    Args:
        BaseCaching ( class ): Parent class
    """
    def __init__(self):
        """ Initialize class instance to empty
        to create new instance of LIFO cache system
        """
        super().__init__()
        self.key_order_tracker = []
# end of init method

    def put(self, key, item):
        """ Add key/value pairs to the cache

        Args:
            key (str): key to add to cache
            item (str): item to add to cache
        """
        # if key and item are not None
        if key is not None and item is not None:
            # do this if key is in cache
            if key in self.cache_data:
                self.cache_data[key] = item
                self.key_order_tracker.remove(key)
            # do this if key is not in cache
            else:
                # if cache is at max capacity
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # pop last element in key_order_tracker
                    lifo_discard = self.key_order_tracker.pop()
                    # delete last element in cache
                    del self.cache_data[lifo_discard]
                    print("DISCARD: {}".format(lifo_discard))
                self.cache_data[key] = item
            self.key_order_tracker.append(key)
        # end of if key and item are not None
    # end of put method

    def get(self, key):
        """ Get value from key in cache """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
    # end of get method
