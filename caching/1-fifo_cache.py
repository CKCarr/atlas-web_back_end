#!/usr/bin/python3
"""
Create a class FIFOCache that inherits from BaseCaching
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
    you must discard the first item put in cache (FIFO algorithm)
    you must print DISCARD:
    with the key discarded and following by a new line

def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data,
    return None.FIFO caching system

    """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache system takes the first element in
        and pops that first element out
        when Max cap is reached

    Args:
        BaseCaching (class): Parent class
    """
    # override init method - add a new variable to track the order of the keys
    def __init__(self):
        """ Initialize FIFOCache object/instance class"""
        # use super() to call init from the parent class
        super().__init__()
        # key_order_tracker - list to keep track of the order of the keys
        self.key_order_tracker = []

    def put(self, key, item):
        """ Add key/value pairs to the cache

        Args:
            key (str): key to add to the cache
            item (str): value to add to the cache
        """
        # check if key or item is not None
        if key is not None and item is not None:
            # check if key is not already in the cache
            if key not in self.cache_data:
                # keep track of order in which keys are added to the cache
                self.key_order_tracker.append(key)
            # add key/value'item' pair to the cache
            self.cache_data[key] = item

            # check if the cache has exceeded the max item limit
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # FIFO - pop(0) 'remove' first element from the cache
                # and remove it from the key order tracker

                # variable to store the key to be removed
                fifo_discard = self.key_order_tracker.pop(0)
                del self.cache_data[fifo_discard]

                # print 'DISCARD:' followed by the key that was removed
                print('DISCARD:', fifo_discard)
# end of put method

    def get(self, key):
        """ Get value from the cache using key
            return the value in self.cache_data linked to key

        Args:
            key ( str ): key to look for in cache
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
# end of get method
