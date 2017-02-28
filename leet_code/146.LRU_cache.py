'''
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following
operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

'''


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key_val = {}
        # keep all keys in cache[]
        self.keys = []

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.key_val:
            self.keys.remove(key)
            self.keys.append(key)
            return self.key_val[key]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """

        if key in self.key_val:
            self.key_val[key] = value
            self.keys.remove(key)
            self.keys.append(key)
        else:
            if len(self.key_val) == self.capacity:
                del self.key_val[self.keys[0]]
                del self.keys[0]

            self.key_val[key] = value
            self.keys.append(key)