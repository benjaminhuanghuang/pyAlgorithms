"""

"""
def insert_sort(number_array):
    length = len(number_array)
    if length < 2:
        return number_array
    for x in xrange(1, length):
        cursor = number_array[x]
        # 算法不是从头开始比较的，而是从Cursor的上一个元素比较的，否则必须使用多个循环。
        for y in reversed(xrange(0, x)):
            if cursor < number_array[y]:  # 一个重要的细节：如果两个元素相等，那么它们的顺序不会变
                # 忽略了一个边界条件cursor=1,而li[0]=2的时候，需要li[0]=cursor
                number_array[y + 1], number_array[y] = number_array[y], cursor
            else:
                number_array[y + 1] = cursor
                break
    return number_array


def reverse_insert_sort(number_array):
    list_len = len(number_array)
    if list_len < 2:
        return number_array
    for x in xrange(1, list_len):
        cursor = number_array[x]
        # 算法不是从头开始比较的，而是从Cursor的上一个元素比较的，负责必须使用多个循环。
        for y in reversed(xrange(0, x)):
            if cursor > number_array[y]:  # 一个重要的细节：如果两个元素相等，那么它们的顺序不会变
                # 忽略了一个边界条件cursor=1,而li[0]=2的时候，需要li[0]=cursor
                number_array[y + 1], number_array[y] = number_array[y], cursor
            else:
                number_array[y + 1] = cursor
                break
    return number_array


def main():
    print reverse_insert_sort([2, 13, 4, 1919, 1, 1100, 1, 2, 3, 373737, 0])


if __name__ == '__main__':
    main()
