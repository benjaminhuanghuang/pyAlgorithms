'''
Divisible Sum Pairs


'''
a = []
k = 3
count = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] + a[j]) % k == 0:
            count += 1

print count
