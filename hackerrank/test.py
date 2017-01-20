def is_anagrams(s1,s2):

    if len(s1) != len(s2):
        return False

    count_dict ={}
    for c in s1:
        count_dict[c] = count_dict.get(c, 0)+1

    for c in s2:
        count = count_dict.get(c, 0)
        if count >0:
            count_dict[c] = count -1
        else:
            return False
    return True



s1='abbb'
s2='bbba'

print is_anagrams(s1,s2)