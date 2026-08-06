from itertools import permutations

print("CRYPT ARITHMETIC PROBLEM")
print("Aadhithya, 192511256")

# Generate permutations of 8 unique digits for letters: S, E, N, D, M, O, R, Y
for p in permutations(range(10), 8):
    S, E, N, D, M, O, R, Y = p

    # Leading letters S and M cannot be zero
    if S != 0 and M != 0:
        send = 1000 * S + 100 * E + 10 * N + D
        more = 1000 * M + 100 * O + 10 * R + E
        money = 10000 * M + 1000 * O + 100 * N + 10 * E + Y

        if send + more == money:
            print("\nSolution Found:")
            print(f"  {send}")
            print(f"+ {more}")
            print("-------")
            print(f" {money}\n")
            print("Letter Mapping:")
            print(
                f"S={S}, E={E}, N={N}, D={D}, M={M}, O={O}, R={R}, Y={Y}"
            )
            break
