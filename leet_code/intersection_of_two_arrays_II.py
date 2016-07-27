'''
350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

import collections

# Solution1 : sort and two-points
def arrays_interseciton_II(nums1, nums2):
    nums1, nums2 = sorted(nums1), sorted(nums2)
    p1 = p2 = 0
    ans = []
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] < nums2[p2]:
            p1 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            ans += nums1[p1],
            p1 += 1
            p2 += 1
    return ans


# Do not need load all nums
# use python library collections
def arrays_interseciton_II_2(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    # dict subclass for counting hashable objects
    c = collections.Counter(nums1)
    ans = []
    for x in nums2:
        if c[x] > 0:
            ans += x,
            c[x] -= 1
    return ans

b1 = [1, 2, 2,  3, 4, 5, 9, 11, 15]
b2 = [4, 5, 2, 2, 6, 7, 8]

print arrays_interseciton_II_2(b1, b2)

