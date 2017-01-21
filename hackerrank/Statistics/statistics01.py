import math


def cal_median(nums):
    median = 0
    n = len(nums)
    if n % 2 == 0:
        median = float(nums[n / 2 - 1] + nums[n / 2]) / 2
    else:
        median = float(nums[n / 2])
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


n = 30
nums = map(int, "10 40 30 50 20 10 40 30 50 20 1 2 3 4 5 6 7 8 9 10 20 10 40 30 50 20 10 40 30 50".split(" "))
fres = map(int, "1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 10 40 30 50 20 10 40 30 50 20".split(" "))


def cal_interquartile_range(nums, fres):
    n = len(nums)
    arr = []
    for i in range(n):
        arr += [nums[i]] * fres[i]

    arr.sort()
    print arr
    n = len(arr)
    if len(arr) % 2 == 0:
        Q1 = cal_median(arr[:n / 2])
        Q3 = cal_median(arr[n / 2:])
    else:
        Q1 = cal_median(arr[:n / 2])
        Q3 = cal_median(arr[n / 2 + 1:])
    print Q1
    print Q3
    print Q3 - Q1


    # cal_interquartile_range(nums, fres)


def cal_standard_deviation(nums):
    n = len(nums)
    mean = sum(nums) / n

    sum = 0
    for i in range(n):
        sum += (nums[i] - mean) ** 2

    sd = math.sqrt(float(sum) / n)
    return round(sd, 1)
