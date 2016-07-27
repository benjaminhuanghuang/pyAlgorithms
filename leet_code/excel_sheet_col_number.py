'''
171. Excel Sheet Column Number
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''


def title_to_number(title):
    result = 0
    for char in title:
        result = result * 26 + ((ord(char) - ord('A') + 1))

    return result
