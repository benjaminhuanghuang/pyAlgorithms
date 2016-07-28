'''
1. find min element in the
'''


def select_sort(items):
    n = len(items)
    for i in range(0, n):
        min = i  # 最小元素下标标记
        for j in range(i + 1, n):
            if items[j] < items[min]:
                min = j  # 找到最小值的下标
        items[min], items[i] = items[i], items[min]  # swap
    return items
