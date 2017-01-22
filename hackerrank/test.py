h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]

# s1 = sum(h1)
# s2 = sum(h2)
# s3 = sum(h3)
# h = -1
# while len(h1) > 0 and len(h2) > 0 and len(h3) > 0:
#     if s1 == s2 and s1 == s3:
#         h = s1
#         break
#     else:
#         if s1 > s2 and s1 > s3:
#             s1 -= h1.pop()
#         elif s2 > s1 and s2 > s3:
#             s2 -= h2.pop()
#         elif s3 > s1 and s3 > s2:
#             s3 -= h3.pop()
# print h

s1 = sum(h1)
s2 = sum(h2)
s3 = sum(h3)
h = -1
i1 = 0
i2 = 0
i3 = 0
while i1 < len(h1) and i2 < len(h2) and i3 < len(h3):
    if s1 == s2 and s1 == s3:
        h = s1
        break
    else:
        if s1 > s2 and s1 > s3:
            s1 -= h1[i1]
            i1 += 1
        elif s2 > s1 and s2 > s3:
            s2 -= h2[i2]
            i2 += 1
        elif s3 > s1 and s3 > s2:
            s3 -= h3[i3]
            i3 += 1
        elif s1 == s2 and s1 > s3:
            s1 -= h1[i1]
            i1 += 1
            s2 -= h2[i1]
            i2 += 1
        elif s2 == s3 and s3 > s1:
            s2 -= h2[i2]
            i2 += 1
            s3 -= h3[i3]
            i3 += 1

print h

h = -1
