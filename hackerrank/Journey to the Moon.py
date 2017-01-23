'''
https://www.hackerrank.com/challenges/journey-to-the-moon?h_r=internal-search
Answer = (axb) + (axc) + (bxc)
       = (axb) + (a+b)xc

Answer = (axb) + (axc) + (axd) + (bxc) + (bxd) + (cxd) =
       = (axb) x (a+b)xc + (a+b+c)xd

answoer = old answer + the sum of old values x new value.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = 10
input = [
    [0, 2],
    [1, 8],
    [1, 4],
    [2, 8],
    [2, 6],
    [3, 5],
    [6, 9]

]
countries = []

for i in range(n):
    countries.append(set([i]))

for i in xrange(7):
    a, b = input[i]
    # Store a and b in an appropriate data structure

    new_contry = set()
    new_contry.add(a)
    new_contry.add(b)
    i = 0
    while i < len(countries):  # do not use for c in countries here!
        if new_contry & countries[i]:
            new_contry = new_contry | countries[i]
            countries.pop(i)
        else:
            i += 1
    countries.append(new_contry)

i = 1
sum = len(countries[0])
result = 0
while i < len(countries):
    if result == 0:
        result = len(countries[i]) * len(countries[i - 1])
        sum += len(countries[i])
    else:
        result = result + sum * len(countries[i])
        sum += len(countries[i])
    i += 1
print result
