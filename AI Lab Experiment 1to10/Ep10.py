print("A* ALGORITHM")
print("Aadhithya, 192511256")

graph = {}
n = int(input("Enter number of nodes: "))

# Build the adjacency list with edge costs
for i in range(n):
    node = input("Node: ")
    graph[node] = {}
    e = int(input("Edges from " + node + ": "))
    for j in range(e):
        v = input("Connected node: ")
        c = int(input("Cost: "))
        graph[node][v] = c

# Input heuristic values for each node
h = {}
for node in graph:
    h[node] = int(input("Heuristic of " + node + ": "))

start = input("Start node: ")
goal = input("Goal node: ")

open_set = [start]
cost = {start: 0}
parent = {start: None}

while open_set:
    # Select node with minimum f(n) = g(n) + h(n)
    x = min(open_set, key=lambda i: cost[i] + h[i])
    open_set.remove(x)

    # Goal check
    if x == goal:
        path = []
        curr = x
        while curr:
            path.append(curr)
            curr = parent[curr]
        
        path.reverse()
        print("\nPath Found:", " -> ".join(path))
        print("Total Cost:", cost[goal])
        break

    # Process neighboring nodes
    for y in graph.get(x, {}):
        g = cost[x] + graph[x][y]
        if y not in cost or g < cost[y]:
            cost[y] = g
            parent[y] = x
            if y not in open_set:
                open_set.append(y)
