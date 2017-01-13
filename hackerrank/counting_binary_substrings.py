# Counting Binary Substrings

import sys
import os


def counting1(s):
    ans = 0
    for i in range(len(s) - 1):
        sub = s[i]
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                sub += s[j]
            else:
                break
        if j + len(sub) <= len(s):
            if s[j: j + len(sub)] == revert(sub):
                ans += 1
    return ans

def counting2(s):
    ans = 0
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            sub = s[i:j+1]
            if match(sub):
                print sub
                ans +=1
    return ans

def match(s):
    if (len(s) %2 !=0):
        return False
    mid = len(s)/2
    return s[0:mid] == revert(s[mid:])

def count(s):
    count1 = 0
    count0 = 0
    for c in s:
        if c == '1':
            count1 += 1
        if c == '0':
            count0 += 1
    return count1 == count0


def revert(s):
    if s[0] == '0':
        return "1" * len(s)
    if s[0] == '1':
        return "0" * len(s)


# f = open(os.environ['OUTPUT_PATH'], 'w')
#
#
# try:
#     _s = raw_input()
# except:
#     _s = None
#
# res = counting(_s)
# f.write(str(res) + "\n")
#
# f.close()


input = "00110"  # 0011, 01, 10
ans = counting2(input)
print ans
