'''
336. Palindrome Pairs

Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the
concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]

Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
'''


# http://bookshadow.com/weblog/2016/03/10/leetcode-palindrome-pairs/
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        def isPalindrome(word):
            size = len(word)
            for x in range(size / 2):
                if word[x] != word[size - x - 1]:
                    return False
            return True

        word_index_dict = {y: x for x, y in enumerate(words)}
        ans = set()
        for idx, word in enumerate(words):
            if "" in word_index_dict and word != "" and isPalindrome(word):
                bidx = word_index_dict[""]
                ans.add((bidx, idx))
                ans.add((idx, bidx))

            rword = word[::-1]
            if rword in word_index_dict:
                ridx = word_index_dict[rword]
                if idx != ridx:
                    ans.add((idx, ridx))
                    ans.add((ridx, idx))

            for x in range(1, len(word)):
                left, right = word[:x], word[x:]
                rleft, rright = left[::-1], right[::-1]
                if isPalindrome(left) and rright in word_index_dict:
                    ans.add((word_index_dict[rright], idx))
                if isPalindrome(right) and rleft in word_index_dict:
                    ans.add((idx, word_index_dict[rleft]))
        return list(ans)


words = ["abcd", "dcba", "lls", "s", "sssll", "s"]
s = Solution()
print s.palindromePairs(words)
