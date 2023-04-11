def isValid(s):
    hashmap = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    stack = []
    for c in s:
        if c in hashmap:
            if stack or hashmap[c] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False
s = '()[]('
print(isValid(s))
