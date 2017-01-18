n = 3
a = [3, 2, 1]

numberOfSwaps = 0
for i in range(n):
    for j in range(n - 1):
        if (a[j] > a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]
            numberOfSwaps += 1

print a

# compare those implements

n = 3
a = [3, 2, 1]

for i in range(n-1, -1, -1):
    for j in range(i):
        if (a[j] > a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]
            numberOfSwaps += 1

print a