def fun():
    pass


f_testcase = open('testcase.txt', 'r')
f_result = open('expect.txt', 'r')
n = int(f_testcase.readline())
for i in range(n):
    s = f_testcase.readline().strip()
    res = fun(s)
    if res == s:
        res = "no answer"
    expect = f_result.readline().strip()
    if res != expect:
        print s + "   " + expect
    else:
        print s + "-------"

f_testcase.close()
f_result.close()
