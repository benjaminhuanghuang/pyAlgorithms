class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        average = sum(self.scores) / len(self.scores)

        if 90 <= average and average <= 100:
            return "O"
        elif 80 <= average and average < 90:
            return "E"
        elif 70 <= average and average < 80:
            return "A"
        elif 55 <= average and average < 70:
            return "P"
        elif 40 <= average and average < 55:
            return "D"
        elif average <= 40:
            return "T"


'''
line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input())  # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()
'''

firstName = "Sancho"
lastName = "Panza"
idNum = '4847677'
scores = map(int, "41 42 43 44 45 46 48".split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()
