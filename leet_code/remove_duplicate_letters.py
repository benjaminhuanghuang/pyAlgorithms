'''
316. Remove Duplicate Letters

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and
only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"


Reference :
    https://www.hrwhisper.me/leetcode-remove-duplicate-letters/
'''
import collections


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        while s:
            cnt = collections.Counter(s)
            min_c, index = s[0], 0
            for i, c in enumerate(s):
                if min_c > c:
                    min_c, index = c, i
                cnt[c] -= 1
                if cnt[c] == 0:
                    break
            ans += min_c
            s = s[index + 1:].replace(min_c, '')
        return ans


input = "bcabc"

s = Solution()
print s.removeDuplicateLetters(input)
