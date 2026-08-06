print("Depth First Search")
print("Aadhithya, 192511256")

visited = []
graph = {}

n = int(input("Enter number of vertices: "))

# Reading graph adjacency list
for i in range(n):
    vertex = input("Enter vertex: ")
    neighbors = input("Enter adjacent vertices (space separated): ").split()
    graph[vertex] = neighbors


def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for i in graph.get(node, []):
            dfs(i)


start = input("\nEnter starting vertex: ")

print("\nDFS Traversal:")
dfs(start)
print()  # For clean newline after output
