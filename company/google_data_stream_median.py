'''
http://www.lintcode.com/en/problem/data-stream-median/

http://weibo.com/ttarticle/p/show?id=2309404057810387248595#_0

http://www.jianshu.com/p/e003872fa7b9
'''

from heapq import heappush, heappop, heapreplace, heappushpop


class Solution:
    def median(self, nums):
        length = len(nums)
        if length == 0:
            return []

        min_heap = [nums[0]]  # min root heap
        max_heap = []  # max root heap
        result = [nums[0]]

        for i in range(1, length):
            if i % 2 == 0:
                if nums[i] > min_heap[0]:  # nums[i]
                    heappush(max_heap, -min_heap[0])
                    heapreplace(min_heap, nums[i])
                else:
                    heappush(max_heap, -nums[i])
            elif i % 2 != 0:
                if nums[i] > min_heap[0]:  # nums[i]
                    heappush(min_heap, nums[i])
                else:
                    max_heap_root = heappushpop(max_heap, -nums[i])
                    heappush(min_heap, -max_heap_root)
            result.append(min_heap[0])

        return result


s = Solution()
nums = [4, 5, 1, 3, 2, 6, 0]
result = s.median(nums)

print result
