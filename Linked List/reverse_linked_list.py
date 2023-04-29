class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)
fifth_node = Node(5)
head.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node

def reverseList(head): 
    prev = None
    curr = head 
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    while prev:
        print(prev.data)
        prev = prev.next

    return next
    

print(reverseList(head))