from collections import deque

print("MISSIONARIES AND CANNIBALS PROBLEM")
print("Aadhithya, 192511256")

# Initial state: (Missionaries on Left, Cannibals on Left, Boat Position)
# Boat Position: 0 = Left bank, 1 = Right bank
q = deque([((3, 3, 0), [])])
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
seen = set()

while q:
    (m, c, b), path = q.popleft()

    if (m, c, b) in seen:
        continue
    seen.add((m, c, b))

    # Goal State: 0 Missionaries, 0 Cannibals on Left Bank, Boat on Right Bank
    if (m, c, b) == (0, 0, 1):
        full_path = path + [(m, c, b)]
        print("\nSolution Path Found:")
        for step, (lm, lc, boat) in enumerate(full_path):
            boat_pos = "Right" if boat == 1 else "Left"
            rm, rc = 3 - lm, 3 - lc
            print(
                f"Step {step}: Left Bank [M:{lm}, C:{lc}] | Boat: {boat_pos} | Right Bank [M:{rm}, C:{rc}]"
            )
        break

    for x, y in moves:
        nm = m - x if b == 0 else m + x
        nc = c - y if b == 0 else c + y

        # Check valid numbers (between 0 and 3)
        if 0 <= nm <= 3 and 0 <= nc <= 3:
            # Check safety: Missionaries must not be outnumbered on either bank
            left_safe = (nm == 0) or (nm >= nc)
            right_safe = ((3 - nm) == 0) or ((3 - nm) >= (3 - nc))

            if left_safe and right_safe:
                q.append(((nm, nc, 1 - b), path + [(m, c, b)]))
