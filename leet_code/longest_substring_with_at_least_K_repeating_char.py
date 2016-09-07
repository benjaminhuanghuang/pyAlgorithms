'''
395. Longest Substring with At Least K Repeating Characters

Find the length of the longest substring T of a given string (consists of lowercase letters only)
such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''

import collections
import re


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = collections.Counter(s)
        filters = [x for x in cnt if cnt[x] < k]
        if not filters:
            return len(s)
        tokens = re.split('|'.join(filters), s)
        return max(self.longestSubstring(t, k) for t in tokens)
        # error!
        # return max(len(t) for t in tokens)


s = "aaabb"
k = 3
s = "aacbabbc"
k = 3

s = "ababacb"
k = 3

solution = Solution()
print solution.longestSubstring(s, k)
