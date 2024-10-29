#!/usr/bin/env python3
"""Basic dictionary """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
caching system without limit
    """

    def __init__(self):
        """
initialize BasicCache
        """
        super().__init__()

    def put(self, key, item):
        """
add an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
get an item by key
        """
        if key is not None:
            if key in self.cache_data:
                return self.cache_data.get(
                    key)
            return None
        return None
