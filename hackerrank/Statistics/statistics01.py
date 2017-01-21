def cal_median(nums):
    median = 0
    n = len(nums)
    if n % 2 == 0:
        median = (nums[n / 2 - 1] + nums[n / 2]) / 2
    else:
        median = nums[n / 2]
    return median


'''
Test Case 1:
10
3 7 8 5 12 14 21 15 18 14

7
13
15
'''

n = 10
nums = map(int, "3 7 8 5 12 14 21 15 18 14".split(" "))

nums.sort()

def cal_quartiles(nums):
    Q2 = cal_median(nums)
    if n % 2 == 0:
        Q1 = cal_median(nums[:n / 2])
        Q3 = cal_median(nums[n / 2:])
    else:
        Q1 = cal_median(nums[:n / 2])
        Q3 = cal_median(nums[n / 2 + 1:])

        print Q1
        print Q2
        print Q3



