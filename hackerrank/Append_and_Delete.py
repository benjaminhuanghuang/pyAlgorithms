import sys

# s = raw_input().strip()
# t = raw_input().strip()
# k = int(raw_input().strip())

s = "aba"
t = "aba"
k = 7

len_s = len(s)
len_t = len(t)
comm_length = 0
while comm_length < min(len_s, len_t):
    if s[comm_length] == t[comm_length]:
        comm_length += 1
    else:
        break

# difference > k
if len_s + len_t - 2 * comm_length > k:
    print "No"
# number of difference is even or odd
elif (len_s + len_t - 2 * comm_length) % 2 == k % 2:
    print "Yes"
elif len_s + len_t - k < 0:
    print "Yes"
else:
    print "No"
