#!/usr/bin/env python3
""" inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ inherits from BaseCaching """

    def put(self, key, item):
        """ add ti cache """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """" get from cache """
        if key is None:
            pass
        elif key not in self.cache_data.keys():
            pass
        elif key in self.cache_data:
            return self.cache_data[key]
