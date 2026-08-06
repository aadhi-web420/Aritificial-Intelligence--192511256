print("BREADTH FIRST SEARCH (BFS)")
print("Aadhithya, 192511256")

visited = []
queue = []
graph = {}

n = int(input("Enter number of vertices: "))

# Reading graph adjacency list
for i in range(n):
    vertex = input("Enter vertex: ")
    neighbors = input("Enter adjacent vertices (space separated): ").split()
    graph[vertex] = neighbors


def bfs(start):
    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        # Process each adjacent vertex
        for i in graph.get(node, []):
            if i not in visited:
                visited.append(i)
                queue.append(i)


start = input("\nEnter starting vertex: ")
print("BFS Traversal:")
bfs(start)
print()  # For clean newline after output
