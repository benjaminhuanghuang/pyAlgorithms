'''
318. Maximum Product of Word Lengths

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not
share common letters.
You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
'''
import collections

class Solution(object):
    # http://blog.csdn.net/friendbkf/article/details/50346299
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """


    # max(O(n^2), O(n*m)) n = count of words, m is average length of words
    # http://bookshadow.com/weblog/2015/12/16/leetcode-maximum-product-word-lengths/
    def maxProduct_1(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        nums = []
        size = len(words)
        for w in words:
            nums += sum(1 << (ord(x) - ord('a')) for x in set(w)),
        ans = 0
        for x in range(size):
            for y in range(size):
                if not (nums[x] & nums[y]):
                    ans = max(len(words[x]) * len(words[y]), ans)
        return ans



s = Solution()
print s.maxProduct_1(["aba", "badd"])