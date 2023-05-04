"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. 
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

class Node():
    def __init__(self, data):
        self.val = data
        self.next = None

def mergeTwoLists(list1, list2):
    dummy = Node(0)
    tail = dummy #tail =  Null

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = Node(list1.val)
            list1 = list1.next
        else:
            tail.next = Node(list2.val)
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    else:
        tail.next = list2

    result = dummy.next

    while dummy.next:
        dummy = dummy.next
        print(dummy.val," -> ", end="")

    return result

# First Linked List
head = Node(1)
second_node = Node(2)
third_node = Node(4)
head.next = second_node
second_node.next = third_node # 1 -> 2 -> 4

# Second Linked List
head2 = Node(1)
second_node2 = Node(3)
third_node2 = Node(4)
head2.next = second_node2
second_node2.next = third_node2  # 1 -> 3 -> 4

# 1 -> 1 -> 2 -> 3 -> 4 -> 4
print(mergeTwoLists(head, head2))



