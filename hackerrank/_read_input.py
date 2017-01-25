n, k, q = raw_input().strip().split(' ')
n, k, q = [int(n), int(k), int(q)]
a = map(int, raw_input().strip().split(' '))

for a0 in xrange(q):
    m = int(raw_input().strip())

# read 5 2
n, q = map(int, raw_input().strip().split(" "))


n = int(raw_input())
nums = map(int, raw_input().strip().split(' '))


n = int(raw_input())

dict = {}
for i in range(n):
    name, num = raw_input().strip().split(' ')
    dict[name] = num

while True:
    try:
        name = raw_input().strip()
        if name in dict:
            print name+"="+dict[name]
        else:
            print "Not found"
    except EOFError:
       break