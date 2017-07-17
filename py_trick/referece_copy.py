n = 3
# Note! [[0] * n] * n has same reference!
matrix1 = [[0] * n] * n
matrix1[0][1] = 1
print matrix1

# different reference
matrix = [[0 for i in range(n)] for j in range(n)]
matrix[0][1] = 2
print matrix

a = [1] * 2
b = [a] * 2

a = [2]
print b

b[1][1] = 3
print b

# parameters are passed by reference or value
a = [1, 2, 3]

def change_element(a):
    # a[0] = 'a'
    a = ['a', 'b', 'c']
change_element(a)
print a
