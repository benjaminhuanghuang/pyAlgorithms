import collections

people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

# by default, sort by the first field of element ascending
people.sort()
print people

# sort by element[0] descending element[1] ascending
people.sort(key=lambda (h, k): (-h, k))
print people

# sort by element[1] ascending
people.sort(key=lambda d: d[1])
print people

# use static method
people = sorted(people, key=lambda e: e[1], reverse=True)
print people

# sort by element[1] descending
people.sort(key=lambda d: d[1], reverse=True)
print people

# filter
t = "target"
s = "source"
for i, c in filter(lambda x: x[1] in t, enumerate(s)):
    pass

nums = [2, 6, 7, 8, 9]
count_dict = collections.Counter(nums)
# sort dict by VALUE
# sorted(count_dict, key=count_dict.__getitem__, reverse=True)   # method 1
sorted(count_dict, key=lambda x: count_dict[x], reverse=True)
