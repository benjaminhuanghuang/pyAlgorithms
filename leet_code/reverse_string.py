'''
344. Reverse string
'''


def reverse_string_pythonic(input_str):
    '''
    This function use Python's slice notation
        array[start:end:step] # start through not past end, by step
    :param input_str:
    :return:
    '''
    return input_str[::-1]

def reverse_string(input_str):
    result = ""
    for i in xrange(len(input_str)-1, -1, -1):
        result += input_str[i]
    return result
