'''
373. Find K Pairs with Smallest Sums

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]

'''


# http://bookshadow.com/weblog/2016/07/07/leetcode-find-k-pairs-with-smallest-sums/
# http://blog.csdn.net/wds2006sdo/article/details/51951753

import heapq

class Solution(object):
    # Memory Limit Exceeded
    def kSmallestPairs_niave(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        res = []
        for e1 in nums1:
            for e2 in nums2:
                res.append([e1, e2])

        res_sum_dict = {}

        for i, e in enumerate(res):
            e_sum = e[0] + e[1]
            res_sum_dict[i] = e_sum

        newdict = sorted(res_sum_dict.items(), key=lambda d: d[1])
        res_list = []
        k = min(k, len(newdict))
        for i in range(k):
            res_list.append(res[newdict[i][0]])
        return res_list

    # http://bookshadow.com/weblog/2016/07/07/leetcode-find-k-pairs-with-smallest-sums/
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        heap = [(0x7FFFFFFF, None, None)]
        size1, size2 = len(nums1), len(nums2)
        idx2 = 0
        while len(ans) < min(k, size1 * size2):
            if idx2 < size2:
                sum, i, j = heap[0]
                # only nums2[idx2] + nums1[0], because nums sorted ascending
                if nums2[idx2] + nums1[0] < sum:
                    for idx1 in range(size1):
                        heapq.heappush(heap, (nums1[idx1] + nums2[idx2], idx1, idx2))
                    idx2 += 1
            sum, i, j = heapq.heappop(heap)
            ans.append((nums1[i], nums2[j]))
        return ans


nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3

nums1 = [1, 1, 2]
nums2 = [1, 2, 3]
k = 10

s = Solution()
print s.kSmallestPairs(nums1, nums2, k)
