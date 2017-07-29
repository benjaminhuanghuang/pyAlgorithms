

def solution(A):
    N = len(A)
    result = 0
    for i in xrange(N):
        for j in xrange(i, N):
            if A[i] != A[j]:
                result = max(result, j - i)
    return result


def solution_better(A):
    N = len(A)
    result = 0
    for i in xrange(N):
        for j in xrange(N-1, i, -1):
            if A[i] != A[j]:
                result = max(result, j - i)
                break
    return result


A = [4,6,2,2,6,6,4]

print solution(A)  # 5
print solution_better(A)  # 5

A = [i for i in range(75001)]
print solution_better(A)