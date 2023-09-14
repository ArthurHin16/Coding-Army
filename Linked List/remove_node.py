# Given the head of a linked list, remove the nth node from the end of the list and return its head.
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(1)
head.next = Node(2)
"""head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)"""

curr = head
while curr:
    print(curr.value, " -> ", end="")
    curr = curr.next

def remove_Nth_From_End(head, n):
    counter = 0
    curr = head
    while curr:
        counter += 1
        curr = curr.next
    print("Counter", counter)

    remove = counter - n
    print("Remove", remove)
    if remove == 0 and counter == 1:
        head = None
    if remove == 0 and counter > 1:
        counter = 0
    else:
        counter = 1
    curr = head
    while curr:
        if counter == remove:
            curr.next = curr.next.next
        counter += 1
        print(curr.value, " -> ", end="")
        curr = curr.next

print("")
print(remove_Nth_From_End(head, 2)) 
