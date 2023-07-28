class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

binary_tree = Node(2)
binary_tree.left = Node(3)
binary_tree.right = Node(4)
binary_tree.left.left = Node(5)
binary_tree.left.right = Node(6)

def preoder_traversal(root):
    result = []
    if not root:
        return result
    stack = [root]
    while stack:
        curr = stack.pop()
        result.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return result

print('Pre-Order Traversal: ', preoder_traversal(root=binary_tree))

def sumed_tree_values(root):
    total_sum = 0
    if not root:
        return total_sum
    stack = [root]
    while stack:
        curr = stack.pop()
        total_sum += curr.val
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return total_sum

print(sumed_tree_values(binary_tree))