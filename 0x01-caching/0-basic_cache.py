#!/usr/bin/env python3
""" basic caching """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ store items """

    def put(self, key, item):
        """ add item """
        if None not in (key, item):
            self.cache_data[key] = item

    def get(self, key):
        """ get item """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
