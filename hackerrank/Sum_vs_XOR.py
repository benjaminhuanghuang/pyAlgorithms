'''

Sum vs XOR

n+x=n ^ x is true
when and only when
n+x= n OR x is true

each 0 bit can XOR with 0 or 1, the answer is 2 ** zeros
'''



# count of 0 bit
count = 0
while n > 0:
    b = n & 1
    if b == 0:
        count += 1
    n = n >> 1
print 1 << count
# print 2 ** count