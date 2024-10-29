#!/usr/bin/python3
""" caching """


class BaseCaching():
    """ BaseCaching defines:
- constants of your caching system
- where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(
                self.cache_data.keys()):
            print("{}: {}".format(
                key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError(
            "put must be implemented i\
                n your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError(
            "get must be implemented i\
                n your cache class")


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
