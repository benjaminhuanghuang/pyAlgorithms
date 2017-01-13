# https://www.hackerrank.com/challenges/sherlock-and-array

def arraySherlock(array):
    l = 0
    r = len(array) - 1

    left_sum = array[l]
    right_sum = array[r]

    while l != r:
        if left_sum < right_sum:
            l += 1
            left_sum += array[l]
        else:
            r -= 1
            right_sum += array[r]

    return left_sum == right_sum


if __name__ == '__main__':
    t = int(raw_input())
    for _ in xrange(t):
        n = int(raw_input())
        a = map(int, raw_input().split())
        if arraySherlock(a):
            print "YES"
        else:
            print "NO"
