#!/usr/bin/python3
""" LRU caching """
from collections import OrderedDict
BaseCaching = __import__(
    'base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
caching system without limit
    """

    def __init__(self):
        """
initialize LRU Cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
add an item to the cache
using LRU caching
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item

            if len(
                    self.cache_data) > BaseCaching.MAX_ITEMS:
                rarely_used_key, _ = self.cache_data.popitem(
                    last=False)
                print("DISCARD:",
                      rarely_used_key)

    def get(self, key):
        """
get an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
