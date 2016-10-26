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
    # https://www.hrwhisper.me/leetcode-maximum-product-of-word-lengths/
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        words_bits = [0] * n
        # create word bits format for each word
        for i, word in enumerate(words):
            for c in word:
                words_bits[i] |= 1 << (ord(c) - 97)

        ans = 0
        for i in xrange(n):
            for j in xrange(i + 1, n):
                if not (words_bits[i] & words_bits[j]):
                    # two words do not have common letter
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans


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