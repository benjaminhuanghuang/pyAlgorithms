# https://www.hackerrank.com/challenges/s10-basic-statistics

# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

# n = int(raw_input())
# nums = map(int, raw_input().strip().split(' '))
n = 10
nums = map(int, "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060".strip().split(" "))

nums.sort()

mean = float(sum(nums)) / n

if n % 2 == 0:
    median = float(nums[n / 2] + nums[n / 2 - 1]) / 2
else:
    median = float(nums[n / 2]) / 2

count_dict = collections.Counter(nums)
# sorted(count_dict, key=count_dict.__getitem__, reverse=True)   # method 1
count_list = sorted(count_dict, key=lambda x: count_dict[x], reverse=True)
mode = count_list[0]
if count_dict[mode] == 1:
    mode = nums[0]


print mean
print median
print mode
