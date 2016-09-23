import heapq

nums = [3, 6, 1, 2, -1, 2, 8]

heapq.heapify(nums)

# pop elements ascending
while nums:
    # pop and return smallest item from the heap
    pop = heapq.heappop(nums)
    print pop

print ""

# python does not has max heap
# reference http://jessicasco.github.io/blog/2015/05/25/python-priority-queue/
nums = [3, 6, 1, 2, -1, 2, 8]
heapq._heapify_max(nums)
while nums:
    # pop and return smallest item from the heap
    pop = heapq.heappop(nums)
    print pop
