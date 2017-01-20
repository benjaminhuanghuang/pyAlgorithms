'''
Super Reduced String
https://www.hackerrank.com/challenges/reduced-string
'''

# s = list(raw_input())
s = list("aaabccddd")
i = 0
while i < len(s) - 1:
    if s[i] == s[i + 1]:
        s.pop(i)
        s.pop(i)
        i = 0
        # if len(s) == 0:
        #     print 'Empty String'
        #     break
    else:
        i += 1

if len(s) == 0:
    print 'Empty String'
else:
    print "".join(s)
