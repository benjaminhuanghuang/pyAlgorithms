from random import randint
def pop_testCase(n):
    for i in range(n):
        no_of_students = randint(1,200)
        threshold = randint(1,no_of_students)
        print str(no_of_students) + " " + str(threshold)
        arrivals = []
        for arrival in range(no_of_students):
            arrivals.append(randint(-1000,1000))
        print " ".join(map(str,arrivals))
print 5
pop_testCase(5)