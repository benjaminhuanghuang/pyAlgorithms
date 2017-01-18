def number_needed(a, b):
    count_dict_a = {}
    count = 0
    for c in a:
        count_dict_a[c] = count_dict_a.get(c, 0) + 1

    for c in b:
        if c in count_dict_a and count_dict_a[c] >= 1:
            count_dict_a[c] -= 1
        else:
            count += 1

    for k, v in count_dict_a.iteritems():
        if v >= 1:
            count += v   # Note! count += 1 is wrong!

    return count


a = "accc"
b = "acc"

a = "fsqoiaidfaukvngpsugszsnseskicpejjvytviya"
b = "ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget"


# res = 42
print number_needed(a, b)
