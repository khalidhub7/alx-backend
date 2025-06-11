#!/usr/bin/python3
""" BaseCaching module """
from collections import OrderedDict


class BaseCaching():
    """
basecaching defines constants
and stores data in a dictionary
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ initiliaze """
        self.cache_data = OrderedDict()

    def print_cache(self):
        """ print the cache """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(
                key, self.cache_data.get(key)
            ))

    def put(self, key, item):
        """ add item to cache """
        raise NotImplementedError(
            "put must be implemented in your cache class"
        )

    def get(self, key):
        """ get item by key """
        raise NotImplementedError(
            "get must be implemented in your cache class"
        )
