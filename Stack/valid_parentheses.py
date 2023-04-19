"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine 
if the input string is valid. An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.
"""
def isValid(parenthesis):
    hashmap = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    stack = []
    for char in parenthesis: 
        if char in hashmap:
            if stack and hashmap[char] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False

parenthesis = '()[]()'
print(isValid(parenthesis))
