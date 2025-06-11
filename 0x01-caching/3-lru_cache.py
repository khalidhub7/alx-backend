#!/usr/bin/env python3
""" LRU caching """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ store items """

    def __init__(self):
        """ initializes """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ add item """
        if None not in (key, item):

            if len(self.cache_data) == self.MAX_ITEMS:
                if key not in self.cache_data:
                    leastUsed, _ = self.cache_data.popitem(
                        last=False
                    )  # returns (key, value) tuple of removed item
                    print(f'DISCARD: {leastUsed}')

            self.cache_data[key] = item
            # move to end since update keeps position
            self.cache_data.move_to_end(key)

    def get(self, key):
        """ get item """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
