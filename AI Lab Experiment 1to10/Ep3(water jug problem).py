import math

print("WATER JUG PROBLEM")
print("Aadhithya, 192511256")

# Input capacities and target
j1 = int(input("Enter capacity of Jug 1: "))
j2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

# Check if target is achievable
if target > max(j1, j2) or target % math.gcd(j1, j2) != 0:
    print("Target cannot be reached with the given jug capacities.")
else:
    a = 0  # Initial amount in Jug 1
    b = 0  # Initial amount in Jug 2

    print(f"\nInitial State: Jug1 = {a}, Jug2 = {b}")

    # Process until target is reached in either jug
    while a != target and b != target:
        if a == 0:
            a = j1  # Fill Jug 1
        elif b == j2:
            b = 0   # Empty Jug 2
        else:
            # Pour water from Jug 1 to Jug 2
            t = min(a, j2 - b)
            a -= t
            b += t

        print(f"Jug1 = {a}, Jug2 = {b}")

    print("Target Reached!")
