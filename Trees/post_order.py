import math

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postOrderTraversal(root):
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        curr = stack.pop()
        result.insert(0, curr.value)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return result


def maxDepth(root):
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    size = len(result)
    print(size)
    if size > 2:
        size = math.ceil(size / 2)
    else:
        return size
    print(size)
    return size


raiz = Node(1)
raiz.right = Node(2)
print(postOrderTraversal(raiz))
print(maxDepth(raiz))
