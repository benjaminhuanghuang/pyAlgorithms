def get_lex_greater(s):
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i + 1]:
            break
        i -= 1
    if i == -1:
        return s
    res = s[:i] + "".join(sorted(s[i:], reverse=True))
    return res


print get_lex_greater("dkhc")
