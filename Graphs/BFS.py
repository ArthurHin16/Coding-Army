"""
ALGORITHM
1. Keep a queue containing the people to check
2. Pop a person off the queue
3. Check if this person is a mango seller
    Case False: Add all their neighbors to the queue
    Case True: You are done!
5. LOOP
6. If the queue is empty, there are no mango sellers in your network
"""
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]
graph["peggy"] = []
graph["anuj"] = []
graph["jonny"] = []
graph["thom"] =[]

def lookig_mango_seller(graph):
    search_queue = deque(graph["you"])
    checked = set()
    def is_mango_seller(person):
        return person[-1] == 'e'
    while search_queue:
        person = search_queue.popleft()
        if person not in checked:
            if is_mango_seller(person):
                print(person + " is a Mango Seller")
                return True
            else:
                search_queue += graph[person]
                checked.add(person)
    print("Sorry there is nobody")
    return False

print(lookig_mango_seller(graph))

