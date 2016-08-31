'''
275. H-Index II

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

'''


class Solution(object):
    # https://www.hrwhisper.me/leetcode-h-index-h-index-ii/
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l, r, n = 0, len(citations), len(citations)
 
        while l < r:
            mid = (l + r) >> 1
            if n - mid <= citations[mid]:
                r = mid
            else:
                l = mid + 1
 
        return n - l
