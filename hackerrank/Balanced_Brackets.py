'''
Balanced Brackets


'''


def is_matched(expression):
    stack = []
    for c in expression:
        if c == "{" or c == "[" or c == "(":
            stack.append(c)
        if c == "}":
            if len(stack) == 0 or stack[-1] != "{":
                return False
            else:
                stack.pop()
        if c == "]":
            if len(stack) == 0 or stack[-1] != "[":
                return False
            else:
                stack.pop()
        if c == ")":
            if len(stack) == 0 or stack[-1] != "(":
                return False
            else:
                stack.pop()


input = "{{[[(())]]}}"
input = "{[(])}"
input = "{[}])}"
print is_matched(input)
