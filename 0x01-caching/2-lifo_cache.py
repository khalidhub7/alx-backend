#!/usr/bin/python3
""" LIFO caching """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
caching system without limit
    """

    def __init__(self):
        """
initialize LIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """
add an item to the cache
using LIFO caching
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.cache_data[key] = item
            elif key in self.cache_data:
                self.cache_data.pop(key)
                self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print('DISCARD: {}'.format(
                    list(self.cache_data.keys())[-2]))
                self.cache_data.pop(
                    list(self.cache_data.keys())[-2])

    def get(self, key):
        """
get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
