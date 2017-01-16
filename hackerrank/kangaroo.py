# https://www.hackerrank.com/challenges/kangaroo?h_r=next-challenge&h_v=zen
import sys

x1, v1, x2, v2 = 0, 3, 4, 2
if x1 >= x2:
    if v2 >= v1 and (x1 - x2) % (v2 - v1) == 0 and (x1 - x2) / (v2 - v1) <= (10000 - x1) / v1:
        print "YES"
        sys.exit()

if x2 >= x1:
    if v1 >= v2 and (x2 - x1) % (v2 - v1) == 0 and (x2 - x1) / (v1 - v2) <= (10000 - x2) / v2:
        print "YES"
        sys.exit()

print "NO"
