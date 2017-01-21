'''
Lexicographically Greater String

leetcode 31. Next Permutation

'''


def get_lex_greater(word):
    if len(word) == 1:
        return word
    s = list(word)
    # from right to left, find out the "first" number it is less than the adjacent number at right side
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i + 1]:
            break
        i -= 1
    # if all number arranges descending, no greater word
    if i == -1:
        return word

    # The right section of the numbers are in descending order
    # find smallest number (bigger than nums[i])in the right section of the numbers

    for j in range(len(s) - 1, i, -1):
        if s[j] > s[i]:
            break

    s[j], s[i] = s[i], s[j]
    # reverse the right section
    s[:] = s[:i + 1] + s[:i:-1]

    return "".join(s)


# print get_lex_greater("zyyxwwtrrnmlggfeb")

f_testcase = open('testcase.txt', 'r')
f_result = open('expect.txt', 'r')
n = int(f_testcase.readline())
for i in range(n):
    s = f_testcase.readline().strip()
    res = get_lex_greater(s)
    if res == s:
        res = "no answer"
    expect = f_result.readline().strip()
    if res != expect:
        print s + "   " + expect
    else:
        print s + "-------"

f_testcase.close()
f_result.close()
