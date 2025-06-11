#!/usr/bin/env python3
""" FIFO caching """
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ store items """

    def __init__(self):
        """ initializes """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ add item """
        if None not in (key, item):
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                firstIn, _ = self.cache_data.popitem(
                    last=False
                )  # returns (key, value) tuple of removed item
                print(f'DISCARD: {firstIn}')

    def get(self, key):
        """ get item """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
