
'''
    decimal zip
'''
def solution (A, B):
    strA = str(A)
    strB = str(B)
    iA = 0
    iB = 0

    res = []
    while(iA < len(strA) or iB < len(strB)):
        if (iA < len(strA)):
            res.append(strA[iA])
            iA +=1
        if (iB < len(strB)):
            res.append(strB[iB])
            iB+=1

    if iA < len(strA):
        res.extend(strA[iA:])
    if iB < len(strB):
        res.extend(strB[iB:])

    return int("".join(res))


A = 12345
B = 678

C = 16273845

print solution(A, B)



