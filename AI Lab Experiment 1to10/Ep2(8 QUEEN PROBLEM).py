print("8 QUEEN PROBLEM")
print("Aadhithya,192511256")
N = int(input("Enter the number of queens: "))

x = [-1] * N

def safe(r, c):
    for i in range(c):
        if x[i] == r or abs(x[i] - r) == abs(i - c):
            return False
    return True

def queen(c):
    if c == N:
        print("\nSolution:")
        for i in range(N):
            print(x[i], end=" ")
        return True

    for r in range(N):
        if safe(r, c):
            x[c] = r
            if queen(c + 1):
                return True
    return False

if not queen(0):
  print("No Solution")
