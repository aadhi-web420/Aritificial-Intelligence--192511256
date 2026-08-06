from itertools import permutations

print("TRAVELLING SALESMAN PROBLEM")
print("Aadhithya, 192511256")

# Distance matrix representing cost between cities 0, 1, 2, and 3
d = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]

cost = float("inf")
path = ()

# Permutations of intermediate cities (1, 2, 3), starting and ending at city 0
for p in permutations([1, 2, 3]):
    c = d[0][p[0]] + d[p[0]][p[1]] + d[p[1]][p[2]] + d[p[2]][0]
    if c < cost:
        cost = c
        path = (0,) + p + (0,)

print("\nShortest Path:", " -> ".join(map(str, path)))
print("Minimum Cost:", cost)
