"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
    - The valid operators are '+', '-', '*', and '/'.
    - Each operand may be an integer or another expression.
    - The division between two integers always truncates toward zero.
    - There will not be any division by zero.
    - The input represents a valid arithmetic expression in a reverse polish notation.
    - The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""
def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in ['+','-','*','/']:
            value1 = stack.pop()
            value2 = stack.pop() 
            if token == '+':
                total = value1 + value2
                stack.append(total)
            elif token == '-':
                total = value2 - value1
                stack.append(total)
            elif token == '*':
                total = value1 * value2
                stack.append(total)
            elif token == '/':
                total = int(value2/ value1)
                stack.append(total)
        else:
            stack.append(int(token))
    return stack[0]

tokens = ["4","13","5","/","+"]
print(evalRPN(tokens))