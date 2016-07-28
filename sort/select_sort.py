'''
1. find the smallest item in the array and exchange it with the first entry
    (itself if the first entry is already the smallest)
2. find the next smallest item and exchange it with the second entry

3. Continue in this way until the entire array is sorted
'''

from utilities.data_generator import *

# N^2/2 compares and N exchanges
def select_sort(items):
    n = len(items)
    for i in range(0, n):
        min_index = i  # index of minimal entry
        for j in range(i + 1, n):
            if items[j] < items[min_index]:
                min_index = j  # get index of the smallest item [j, n-1]
        items[min_index], items[i] = items[i], items[min_index]  # swap
    return items


if __name__ == "__main__":
    random_nums = generate_random_list()
    print random_nums

    print select_sort(random_nums)
