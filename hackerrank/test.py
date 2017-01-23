'''
Answer =(axb) + (axc) + (bxc)
Answer = (axb) + (a+b)xc

Answer = (axb) + (axc) + (axd) + (bxc) + (bxd) + (cxd) =
       = (axb) x (a+b)xc + (a+b+c)xd
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
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
result = 0
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

for c in countries:
    if result == 0:
        result = len(c)
    else:
        result *= len(c)
print result
