'''
Between Two Sets

input:
1 1
1
100
output:
9

-------------
input:
1 2
1
72, 48
output:



'''
n = 1
m = 1
a = [1]
b = [100]

''' My Wrong Answer
res = set()
for a1 in a:
    for a2 in a:
        x = a1*a2
        for n in b:
            if n % x ==0:
                res.add(x)


print len(res)
'''

n = 2
m = 3
a = [2, 4]
b = [16, 32, 96]
# res = 3

b_min = min(b)
a_max = max(a)

count = 0
for i in range(a_max, b_min + 1):
    is_x = True
    for num in a:
        if i % num != 0:
            is_x = False
            break
    for num in b:
        if num % i != 0:
            is_x = False
            break
    if is_x:
        count += 1
print count
