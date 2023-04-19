"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
    - MinStack() initializes the stack object.
    - void push(int val) pushes the element val onto the stack.
    - void pop() removes the element on the top of the stack.
    - int top() gets the top element of the stack.
    - int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""

class MinStack():
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        if len(self.stack) == 1:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

#["MinStack","push","push","push","getMin","pop","top","getMin"]
my_stack = MinStack()
my_stack.push(-2)
my_stack.push(0)
my_stack.push(-3)
print(my_stack.getMin())
my_stack.pop()
print(my_stack.top())
print(my_stack.getMin())
