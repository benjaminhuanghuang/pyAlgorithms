'''
381. Insert Delete GetRandom O(1) - Duplicates allowed

Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being
returned is linearly related to the number of same value the collection contains.
'''
import random
import collections

class RandomizedCollection(object):
    def __init__(self):

        """
        Initialize your data structure here.
        """
        self.index = collections.defaultdict(set)
        self.values = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        return_val = val not in self.index
        self.index[val].add(len(self.values))
        self.values.append(val)
        return return_val

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            return False
        last = self.values.pop()
        self.index[last].remove(len(self.values))
        if val != last:
            index = self.index[val].pop()
            self.index[last].add(index)
            self.values[index] = last
        if not self.index[val]:
            del self.index[val]
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.values[random.randint(0, len(self.values) - 1)]



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()