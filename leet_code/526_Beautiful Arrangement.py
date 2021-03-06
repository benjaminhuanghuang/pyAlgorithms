'''
526. Beautiful Arrangement

Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed
by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Now given N, how many beautiful arrangements can you construct?

Example 1:
Input: 2
Output: 2
Explanation:

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
Note:
N is a positive integer and will not exceed 15.
'''


class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache = dict()

        def solve(idx, nums):
            if not nums:
                return 1
            key = idx, tuple(nums)
            if key in cache:
                return cache[key]
            ans = 0
            for i, n in enumerate(nums):
                if n % idx == 0 or idx % n == 0:
                    ans += solve(idx + 1, nums[:i] + nums[i + 1:])
            cache[key] = ans
            return ans

        return solve(1, range(1, N + 1))


# DFS Solution
# http://massivealgorithms.blogspot.com/2017/02/leetcode-526-beautiful-arrangement.html
# http://www.itwendao.com/article/detail/268726.html

class Solution_DFS(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        used = [False for _ in range(N)]

        return self.backtrack(used, 0)

    def backtrack(self, used, curIndex):
        if curIndex == len(used):
            return 1  # why return 1 here?
        sum = 0
        for i in range(len(used)):
            if (not used[i] and
                    ((i + 1) % (curIndex + 1) == 0 or (curIndex + 1) % (i + 1) == 0)):
                used[i] = True
                sum += self.backtrack(used, curIndex + 1)
                used[i] = False
        return sum


s = Solution()

print s.countArrangement(6)

s = Solution_DFS()

print s.countArrangement(6)
