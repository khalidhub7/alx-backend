#!/usr/bin/env python3
""" LFU caching """
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ store items """

    def __init__(self):
        """ initializes """
        super().__init__()
        self.cache_data = OrderedDict()
        self.FrequencyUsed = OrderedDict()

    def put(self, key, item):
        """ add item """
        if None not in (key, item):
            if key not in self.cache_data:
                if len(self.cache_data) == self.MAX_ITEMS:
                    leastFrequentlyUsed = min(
                        self.FrequencyUsed, key=self.FrequencyUsed.get
                    )
                    self.cache_data.pop(leastFrequentlyUsed)
                    self.FrequencyUsed.pop(leastFrequentlyUsed)
                    print(f'DISCARD: {leastFrequentlyUsed}')
            self.cache_data[key] = item
            counter = self.FrequencyUsed.get(key, 0) + 1
            self.FrequencyUsed[key] = counter

    def get(self, key):
        """ get item """
        if key in self.cache_data:
            self.FrequencyUsed[key] += 1
            return self.cache_data[key]
        return None
