# parameters are passed by reference or value
l = [1, 2, 3]

def change_element(l):
    # l[0] = 'a'
    l = ['a', 'b', 'c']
change_element(l)
print l


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

# by default, sort by the first field of element ascending
people.sort()
print people

# sort by element[0] descending element[1] ascending
people.sort(key=lambda (h, k): (-h, k))
print people

# sort by element[1] ascending
people.sort(key=lambda d: d[1])
print people