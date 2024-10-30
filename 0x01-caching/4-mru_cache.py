#!/usr/bin/python3
""" MRU caching """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
caching system without limit
    """

    def __init__(self):
        """
initialize MRU Cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
add an item to the cache
using MRU caching
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data
                   ) > BaseCaching.MAX_ITEMS:
                recently_used = list(
                    self.cache_data.keys())[-2]
                self.cache_data.pop(
                    recently_used)
                print("DISCARD: ".format(
                    recently_used))

    def get(self, key):
        """
get an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
