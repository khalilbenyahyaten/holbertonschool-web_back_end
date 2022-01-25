#!/usr/bin/env python3
""" inherits from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ fifoCache """
    def __init__(self):
        """ Init """
        super().__init__()

    def put(self, key, item):
        """ add or update """
        if key is None or item is None:
            pass
        elif len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS \
                and key not in self.cache_data.keys():
            print('DISCARD: ', end='')
            print(list(self.cache_data)[0])
            self.cache_data.pop(list(self.cache_data)[0])
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item

    def get(self, key):
        """" get item """
        if key is None:
            pass
        elif key not in self.cache_data.keys():
            pass
        elif key in self.cache_data:
            return self.cache_data[key]
