"""
    n−1 passes will be made to sort a list of size n
    pass 1 compare n-1 times,
    pass 2 compare n-2 time,
    ..
    pass n - 1 compare 1

    The total number of comparisons is the sum of the first n−1 integers.
    Because the sum of the first n integers is 1/2n^2 + 1/2n, the sum of the first n−1 integers is
    1/2n^2 + 1/2n, which is 1/2n^2 - 1/2n. This is still O(n2) comparisons.
"""

def bubble_sort(num_array):
    length = len(num_array)
    for x in xrange(0, length - 1):
        big_value = num_array[x]
        index = x
        for y in xrange(x + 1, length):
            if big_value >= num_array[y]:
                big_value = num_array[y]
                index = y
        num_array[x], num_array[index] = num_array[index], num_array[x]
    return num_array


def bubbleSort(num_array):
    for passnum in range(len(num_array) - 1, 0, -1):
        for i in range(passnum):
            if num_array[i] > num_array[i + 1]:
                num_array[i], num_array[i + 1] = num_array[i + 1], num_array[i]
    return num_array

def main():
    print bubble_sort([2, 1, 3, 0, 3837, 1, 33, 464])
    print bubbleSort([2, 1, 3, 0, 3837, 1, 33, 464])


if __name__ == '__main__':
    main()
