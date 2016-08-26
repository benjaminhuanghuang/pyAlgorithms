'''
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5


Hints:
    Generalize this question to "Kth element in 2 sorted arrays".
    Median : If there is an odd number of numbers, the middle one is picked.
             If there are an even number of numbers, the median is the mean of the two middle values.
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1) + len(nums2)

        if m % 2 == 1:
            return self.kth(nums1, nums2, m / 2)
        else:
            return float(self.kth(nums1, nums2, m / 2) + self.kth(nums1, nums2, m / 2 - 1)) / 2

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]

        midA, midB = len(a) / 2, len(b) / 2

        if midA + midB < k:
            if a[midA] > b[midB]:
                return self.kth(a, b[midB + 1:], k - midB - 1)
            else:
                return self.kth(a[midA + 1:], b, k - midA - 1)
        else:
            if a[midA] > b[midB]:
                return self.kth(a[:midA], b, k)
            else:
                return self.kth(a, b[:midB], k)
