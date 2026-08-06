print("8 PUZZLE PROBLEM")
print("Aadhithya V ,192511256")
goal = [1,2,3,4,5,6,7,8,0]

print("Enter the initial state (9 numbers):")
state = list(map(int, input().split()))

if state == goal:
   print("Goal State Reached!")
else:
    count = 0
    for i in range(9):
        if state[i] != goal[i]:
            count += 1
print("Misplaced Tiles =", count)

print("\nInitial State:")
for i in range(0,9,3):
    print(state[i:i+3])

print("\nGoal State:")
for i in range(0,9,3):
    print(goal[i:i+3])
