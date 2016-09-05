'''
233. Number of Digit One

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less
than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

'''


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones = 0
        m = 1
        while m <= n:
            a = n / m
            b = n % m
            # (a + 8) /10  handle the case >=2
            ones += (a + 8) / 10 * m
            if a % 10 == 1:
                ones += b + 1
            m *= 10
        return ones

    # http://shaowei-su.github.io/2015/11/29/leetcode233/
    def countDigitOne_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        # ones[x] = how many 1s in range [0, 10 ^ x)
        # ones[1] 0 ~ 9 = 1
        # ones[2] 0 ~ 99 = (0-9)1, 1(0-9)  note: 11 have tow 1s
        # ones[3] 0 ~ 999 = ones[2](0-9) + 1(0-99)
        ones, x = [0], 0
        max_int = (1 << 32) - 1
        while 10 ** x < max_int:
            ones.append(ones[x] * 10 + 10 ** x)
            x += 1

        count, size = 0, len(str(n))
        for digit in str(n):
            digit = int(digit)
            size -= 1
            n -= digit * 10 ** size
            if digit == 1:
                count += ones[size] + 1 + n
            elif digit > 1:
                count += digit * ones[size] + 10 ** size
        return count

    def list_ones(self, n):
        count = 0
        for i in xrange(1, n + 1):
            if (i == 1 or i % 10 == 1 or i / 10 == 1):
                print i
                count += 1
        print "count: ", count


s = Solution()
print s.countDigitOne_2(20)

s.list_ones(13)
