#!/usr/bin/python3
""" LFU caching """
from collections import Counter, OrderedDict
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
        self.usage_order = OrderedDict()

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
                       ) >= BaseCaching.MAX_ITEMS:
                    rarelyused = min(
                        self.most_used,
                        key=self.most_used.get)

                    self.cache_data.pop(
                        rarelyused)
                    self.most_used.pop(
                        rarelyused)

                    print("DISCARD: {}".format(
                        rarelyused))
                self.cache_data[key] = item
                self.most_used[key] = 1

            self.usage_order[key] = self.most_used[key]
            self.usage_order.move_to_end(key)

    def get(self, key):
        """
get an item by key
        """
        if key is not None and key in self.cache_data:
            self.most_used[key] += 1
            self.usage_order[key] += 1
            self.usage_order.move_to_end(key)
            return self.cache_data[key]
        return None
