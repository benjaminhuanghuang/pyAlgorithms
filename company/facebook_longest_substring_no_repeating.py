'''

http://blog.gainlo.co/index.php/2016/10/07/facebook-interview-longest-substring-without-repeating-characters/

Given a string, find the longest substring without repeating characters.
For example, for string "abccdefgh", the longest substring is "cdefgh".

1. It's important to validate the input in the beginning
2. edge cases
3.
4. Write same test cases
'''
def longest_substring(s):
    if not s:
        return None

    start = 0
    end = 0

    longest = ''
    char_set = set()

    while end < len(s):
        end += 1
        curr_char = s[end - 1]
        if curr_char not in char_set:
            char_set.add(curr_char)
            # update the longest string if needed
            if end - start > len(longest):
                longest = s[start:end]
        else:
            while start < end - 1:
                # pop all the chars until find the duplicate char
                if s[start] != curr_char:
                    char_set.remove(s[start])
                    start += 1
                else:
                    start += 1

    return longest


s = 'abccdefgh'
res = longest_substring(s)
print res
