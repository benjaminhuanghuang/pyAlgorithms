'''
315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property
where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].

Reference:
    # http://bookshadow.com/weblog/2015/12/06/leetcode-count-of-smaller-numbers-after-self/
'''


class Solution(object):
    # http://bookshadow.com/weblog/2015/12/06/leetcode-count-of-smaller-numbers-after-self/
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                len_f, len_r = len(left), len(right)
                l = r = 0
                while l < len_f or r < len_r:
                    if r == len_r or l < len_f and left[l][1] <= right[r][1]:
                        enum[l + r] = left[l]
                        result[left[l][0]] += r
                        l += 1
                    else:
                        enum[l + r] = right[r]
                        r += 1
            return enum

        result = [0] * len(nums)
        sort(list(enumerate(nums)))
        return result


nums = [5, 2, 6, 1]
s = Solution()
print s.countSmaller(nums)
