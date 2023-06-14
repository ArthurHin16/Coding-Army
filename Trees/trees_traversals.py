class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorderTraversal(root):
    # Root -> left -> right
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def inorderTraversal(root): #Left -> Root -> Right
    result = []
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result

def postorderTraversal(root): #Left -> Right -> Root
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.insert(0, node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result

"""
Tree
         4
       /   \ 
      2      5
    /   \   /  \         
   1    7  3    8
"""

root = Node(4)
root.left  = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(7)
root.right.left = Node(3)
root.right.right = Node(8)
print(preorderTraversal(root)) #Result [4, 2, 1, 7, 5, 3, 8]
print(inorderTraversal(root)) #Result [1, 2, 7, 4, 3, 5, 8]
print(postorderTraversal(root)) # Result [1, 7, 2, 3, 8, 5, 4]
