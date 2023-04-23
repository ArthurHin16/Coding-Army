"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
We are going to solve this problem by using recursion and backtracking. 
RULES (Backtracking):
    - only add open parenthesis if open < n
    - only add a closing parenthesis if closed < open
    - valid if open == closed == open
"""
def generateParenthesis(n):
    stack = [] # Stack to hold the parenthesis
    res = [] # append the results
    
    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return
        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()
    
    backtrack(0,0)
    return res
n = 3
print(generateParenthesis(n))