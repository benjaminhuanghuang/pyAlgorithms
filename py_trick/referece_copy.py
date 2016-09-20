n = 3
# Note! [[0] * n] * n has same reference!
matrix1 = [[0] * n] * n

## Note! [[0] * n] * n has same reference!
matrix = [[0 for i in range(n)] for j in range(n)]

matrix1[0][1] = 1

print matrix1

a = [1] * 2
b = [a] * 2
a = [2]

print b

b[1][1] = 3

print b
