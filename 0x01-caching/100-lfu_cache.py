#!/usr/bin/python3
""" LFU caching """
from collections import Counter
BaseCaching = __import__(
    'base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
caching system without limit
    """

    def __init__(self):
        """
initialize LFU Cache
        """
        super().__init__()
        self.most_used = Counter()

    def put(self, key, item):
        """
add an item to the cache using LFU caching
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.most_used[key] += 1
            else:
                if len(self.cache_data
                       ) >= self.MAX_ITEMS:

                    rarely_used = min(
                        self.most_used,
                        key=self.most_used.get)

                    self.cache_data.pop(
                        rarely_used)
                    self.most_used.pop(
                        rarely_used)
                    print('DISCARD: {}'
                          .format(rarely_used))
                self.cache_data[key] = item
                self.most_used[key] = 1

    def get(self, key):
        """
get an item by key
        """
        if key is not None and key in self.cache_data:
            self.most_used[key] += 1
            return self.cache_data[key]
        return None
