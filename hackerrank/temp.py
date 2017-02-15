import re

test_string = ('A regular expression is a pattern which specifies a set of strings of characters; '
               'it is said to match certain strings. regular')

f = re.findall(r'regular', test_string)  # ['regular']

print f
# print re.findall(r'strings\.', test_string)  # ['strings.']