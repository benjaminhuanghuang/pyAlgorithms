'''
42. Trapping Rain Water


Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

reference
    http://www.cnblogs.com/zuoyuan/p/3781453.html
    http://www.lxway.net/898969464.html

'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftmosthigh = [0 for i in range(len(height))]
        leftmax = 0
        for i in range(len(height)):
            if height[i] > leftmax:
                leftmax = height[i]
            leftmosthigh[i] = leftmax

        sum = 0
        rightmax = 0
        for i in reversed(range(len(height))):
            if height[i] > rightmax:
                rightmax = height[i]
            if min(rightmax, leftmosthigh[i]) > height[i]:
                sum += min(rightmax, leftmosthigh[i]) - height[i]
        return sum
