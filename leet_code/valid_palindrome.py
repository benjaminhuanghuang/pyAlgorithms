'''
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.


'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1

            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

    def isPalindrome_lazy(self, s):
        new = []
        s = s.lower()  # A..Z to a..z

        for i in s:
            if '0' <= i <= '9' or 'a' <= i <= 'z':
                new.append(i)

        return new == new[::-1]


s = Solution()

print s.isPalindrome("......")
