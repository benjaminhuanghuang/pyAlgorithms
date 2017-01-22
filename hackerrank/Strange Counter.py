'''
t    rem
1-3  3-1
4-9  6-1
10-? 12-1

'''


t = 100
rem = 3
while t > rem:
    t = t - rem
    rem *= 2

print rem - t + 1
