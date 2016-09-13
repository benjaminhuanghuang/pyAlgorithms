'''
307. Range Sum Query - Mutable

Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.


reference:
http://www.cnblogs.com/yrbbest/p/5056739.html
http://bookshadow.com/weblog/2015/11/18/leetcode-range-sum-query-mutable/

Binary Index Tree / Fenwick Tree
https://www.zybuluo.com/Yano/note/320858

segment tree
http://www.cnblogs.com/shuaiwhu/archive/2012/04/22/2464583.html

'''


# Binary Indexed Tree / Fenwick Tree
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums = [0] * (len(nums) + 1)
        self.nums = nums
        self.n = len(nums)
        for i in xrange(len(nums)):
            self.add(i + 1, nums[i])

    def add(self, x, val):
        while x <= self.n:
            self.sums[x] += val
            x += self.lowbit(x)

    def lowbit(self, x):
        return x & -x

    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sums[x]
            x -= self.lowbit(x)
        return res

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.add(i + 1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums:
            return 0
        return self.sum(j + 1) - self.sum(i)


class Segment_Tree(object):
    def add(self, start, end, llist):
        self.start = start
        self.end = end
        self.middle = (start + end) / 2
        self.num = 0

        if self.start + 1 == self.end:
            self.num = llist[self.start]
            return self.num
        else:
            left = Segment_Tree()
            self.left = left
            self.num += left.add(start, self.middle, llist)

            right = Segment_Tree()
            self.right = right
            self.num += right.add(self.middle, end, llist)

            return self.num

    def update(self, index, num):
        if self.start == index and self.start + 1 == self.end:
            cha = num - self.num
            self.num = num
            return cha

        if index >= self.middle:
            cha = self.right.update(index, num)
            self.num += cha
            return cha
        else:
            cha = self.left.update(index, num)
            self.num += cha
            return cha

    def sum(self, start, end):
        if start == self.start and end == self.end:
            return self.num

        if end <= self.middle:
            return self.left.sum(start, end)
        elif start >= self.middle:
            return self.right.sum(start, end)
        else:
            left_val = self.left.sum(start, self.middle)
            right_val = self.right.sum(self.middle, end)

            return left_val + right_val


class NumArray_Segment_Tree(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """

        if len(nums) == 0:
            nums.append(0)

        self.nums = nums
        self.st = Segment_Tree()
        self.st.add(0, len(self.nums), self.nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.st.update(i, val)
        return val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.st.sum(i, j + 1)
