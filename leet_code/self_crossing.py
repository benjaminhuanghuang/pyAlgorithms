'''

You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1]
metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move
your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

Example 1:
    Given x = [2, 1, 1, 2],
    Return true (self crossing)

Example 2:
    Given x = [1, 2, 3, 4],
    Return false (not self crossing)

Example 3:
    Given x = [1, 1, 1, 1],
    Return true (self crossing)
'''


# https://www.hrwhisper.me/leetcode-self-crossing/
class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        for i in xrange(3, len(x)):
            # Case 1: current line crosses the line i-3
            if x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]:
                return True
            # Case 2: current line overlapped line i-4
            elif i >= 4 and x[i - 1] == x[i - 3] and x[i] + x[i - 4] >= x[i - 2]:
                return True
            # Case 3: current line crosses the line i-6 steps ahead of it
            elif i >= 5 and x[i - 2] >= x[i - 4] and x[i] + x[i - 4] >= x[i - 2] and \
                            x[i - 1] <= x[i - 3] and x[i - 1] + x[i - 6] >= x[i - 3]:
                return True

        return False


s = Solution()

x = [2, 1, 1, 2]
print s.isSelfCrossing(x)

x = [1, 2, 3, 4]
print s.isSelfCrossing(x)

x = [1, 1, 1, 1]
print s.isSelfCrossing(x)

x = [1, 1, 2, 2, 1, 1]
print s.isSelfCrossing(x)
