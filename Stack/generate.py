def isValid(parenthesis):
    hashmap = {
            ')':'(',
            '}':'{',
            ']':'['
            }
    stack = []
    for char in parenthesis:
        if char in hashmap:
            if len(stack) > 0 and hashmap[char] == stack[-1]:
                stack.pop()
            else:
                return False
        if char not in hashmap: 
                stack.append(char)
    return True if len(stack) == 0 else False
s = ')'
print(isValid(s))
