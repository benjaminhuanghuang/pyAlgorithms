'''
A subsequence is a sequence that can be derived from another sequence by deleting some elements without
changing the order of the remaining elements.

https://www.youtube.com/watch?v=NnD96abizww
'''

# n, m = map(int, raw_input().strip().split(' '))
# A = map(int, raw_input().strip().split(' '))
# B = map(int, raw_input().strip().split(' '))

n = 5
m = 6
A = [1, 2, 3, 4, 1]
B = [3, 4, 1, 2, 1, 3]

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):    # note!  start from 1!
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

res = []
x, y = n, m
while x != 0 and y != 0:
    if dp[x][y] == dp[x - 1][y]:
        x -= 1
    elif dp[x][y] == dp[x][y - 1]:
        y -= 1
    else:
        res.append(A[x - 1])
        x -= 1
        y -= 1
print res[::-1]
