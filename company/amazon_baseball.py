def totalScore(blocks, n):
    # WRITE YOUR CODE HERE
    res = 0
    scores = []
    for b in blocks:
        if b == "+":
            score = scores[-2] + scores[-1]
            res += score
            scores.append(score)
        elif b == "Z":
            res -= scores[-1]
            scores.pop(-1)
        elif b == "X":
            score = 2 * scores[-1]
            res += score
            scores.append(score)
        else:
            res += int(b)
            scores.append(int(b))
        print res
    return res


b = [5, -2, 4, 'Z', 'X', 9, '+', "+"]
n = 8
print totalScore(b, n)

print "a----"

b = [1, 2, '+', "Z"]
n = 4
print totalScore(b, n)