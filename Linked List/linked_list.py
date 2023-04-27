class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False

head = Node(1)
second_node = Node(2)
head.next = second_node
second_node.next = head
#print(head.next.data)
#print(head.next.next.data)
print(hasCycle(head))

