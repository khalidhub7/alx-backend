#!/usr/bin/env python3
""" FIFO caching """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
caching system without limit
    """

    def __init__(self):
        """
initialize FIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """
add an item to the cache
using FIFO caching
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(
                    self.cache_data) > BaseCaching.MAX_ITEMS:
                print('DISCARD: {}'.format(
                    list(self.cache_data.keys())[0]))
                self.cache_data.pop(
                    list(self.cache_data.keys())[0])

    def get(self, key):
        """
get an item by key
        """
        if key in self.cache_data and key is not None:
            return self.cache_data[key]
        return None
