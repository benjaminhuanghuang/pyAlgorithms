'''
402. Remove K Digits

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number
is the smallest possible.

Note:
The length of num is less than 10002 and will be >= k.
The given num does not contain any leading zero.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''

import collections


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        size = len(num)
        stack = ['0']
        for x in range(size):
            while stack[-1] > num[x] and len(stack) + k > x + 1:
                stack.pop()
            stack.append(num[x])
        while len(stack) > size - k + 1:
            stack.pop()
        return str(int(''.join(stack)))

    # http://bookshadow.com/weblog/2016/09/18/leetcode-remove-k-digits/
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        size = len(num)
        ans = '0'
        numd = collections.defaultdict(collections.deque)
        for i, n in enumerate(num):
            numd[n].append(i)
        p = 0
        for x in range(size - k):
            for y in '0123456789':
                while numd[y] and numd[y][0] < p:
                    numd[y].popleft()
                if numd[y] and numd[y][0] <= k + x:
                    p = numd[y][0]
                    ans += y
                    numd[y].popleft()
                    break
        return str(int(ans))


num = "1432219"
k = 3
s = Solution()
print s.removeKdigits(num, k)
