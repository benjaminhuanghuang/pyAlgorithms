import sys
def array_bitwise(t, k):
    ans = 0
    for i in range(1, t):
        for j in range(i+1, t+1):
            bw = i & j
            if bw < k:
                ans = max(ans, bw)
    return ans




#
# t = int(raw_input().strip())
# for a0 in xrange(t):
#     n,k = raw_input().strip().split(' ')
#     n,k = [int(n),int(k)]
#     print array_bitwise(t, k)


# print array_bitwise(5, 2)
print array_bitwise(2, 2)