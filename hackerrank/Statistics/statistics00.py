# https://www.hackerrank.com/challenges/s10-basic-statistics

# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

n = int(raw_input())
nums = map(int, raw_input().strip().split(' '))

nums.sort()

mean = float(sum(nums)) / n

if n % 2 == 0:
    median = float(nums[n / 2] + nums[n / 2 - 1]) / 2
else:
    median = float(nums[n / 2]) / 2

count_dict = collections.Counter(nums)

# When we have multiple values have same occurrences, select the smallest one

# sorted(count_dict, key=count_dict.__getitem__, reverse=True)   # method 1
# count_list = sorted(count_dict, key=lambda x: count_dict[x], reverse=True)
# Sorting a dictionary by value then key
sorted_count = [k for k, v in sorted(count_dict.iteritems(), key=lambda (k, v): (-v, k))]
mode = sorted_count[0]

print mean
print median
print mode

# ------- Weighted Mean

n = int(raw_input())
nums = map(int, raw_input().strip().split(' '))
weights = map(int, raw_input().strip().split(' '))

nums_sum = 0
for i in range(n):
    nums_sum += nums[i] * weights[i]
mean = float(nums_sum) / sum(weights)  #

print round(mean, 1)  #
