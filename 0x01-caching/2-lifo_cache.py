#!/usr/bin/env python3
""" LIFO caching """
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ store items """

    def __init__(self):
        """ initializes """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ add item """
        if None not in (key, item):

            if len(self.cache_data) >= self.MAX_ITEMS:
                lastIn, _ = self.cache_data.popitem(
                    last=True
                )  # returns (key, value) tuple of removed item
                print(f'DISCARD: {lastIn}')

            self.cache_data[key] = item

    def get(self, key):
        """ get item """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
