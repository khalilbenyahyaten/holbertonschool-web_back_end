#!/usr/bin/env python3
""" inherits from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ lifoCache """
    def __init__(self):
        ''' Init '''
        super().__init__()

    def put(self, key, item):
        """ Put """
        if key is not None and item is not None:
            length = len(self.cache_data.keys())
            if length + 1 > BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                print('DISCARD: ', end='')
                print(list(self.cache_data)[length - 1])
                self.cache_data.pop(list(self.cache_data)[length - 1])
            if key in self.cache_data.keys():
                self.cache_data.pop(list
                                    (self.cache_data)
                                    [list(self.cache_data).index(
                                        '{}'.format(key))])
            self.cache_data[key] = item

    def get(self, key):
        """ get """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
