'''
66. Plus One
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''


# Passing with first try!
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for index in xrange(len(digits) - 1, -1, -1):
            sum = digits[index] + carry
            carry = sum / 10
            digits[index] = sum % 10

        if carry == 1:
            digits = [1] + digits
        return digits
