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

nums = [2, 2, 6, 6, 7, 8, 9]
count_dict = collections.Counter(nums)
# sort dict by VALUE
# sorted(count_dict, key=count_dict.__getitem__, reverse=True)   # method 1
sorted_keys = sorted(count_dict, key=lambda x: count_dict[x], reverse=True)

# Sorting a dictionary by value (DES) then key (ASE)
sorted_count = [k for k, v in sorted(count_dict.iteritems(), key=lambda (k, v): (-v, k))]
print sorted_count[0]  # 2 not 6

dict = {
    "b":"BBBBBB",
    "a":"AAAAAA",
    "c":"CCCCCC",
    "x":"XXXXXX",
    "y":"YYYYYY",
}
dict_sorted = sorted(dict, key=lambda x: dict[x])
print dict_sorted