from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'F'],
    'C': ['G'],
    'D': [],
    'E': [],
    'F': ['H'],
    'G': ['I'],
    'H': [],
    'I': [],
}

def breadth_first_search(graph, node):
    visited = []
    queue = deque()

    visited.append(node)
    queue.append(node)

    while queue:
        curr = queue.popleft()
        print(curr, end=" ")
        for n in graph[curr]:
            if n not in visited:
                queue.append(n)
                visited.append(n)

def main():
    breadth_first_search(graph, 'A')

main()