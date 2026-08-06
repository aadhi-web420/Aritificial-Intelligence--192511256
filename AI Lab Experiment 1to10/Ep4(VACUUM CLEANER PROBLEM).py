print("VACUUM CLEANER PROBLEM")
print("Aadhithya, 192511256")

A = input("Enter Room A status (Dirty/Clean): ").strip()
B = input("Enter Room B status (Dirty/Clean): ").strip()

print("\nInitial State")
print("Room A =", A)
print("Room B =", B)

print("\nVacuum starts at Room A")

# Check and clean Room A
if A.lower() == "dirty":
    print("Room A is Dirty")
    print("Cleaning Room A...")
    A = "Clean"
else:
    print("Room A is already Clean")

# Move to Room B
print("\nMove to Room B")

# Check and clean Room B
if B.lower() == "dirty":
    print("Room B is Dirty")
    print("Cleaning Room B...")
    B = "Clean"
else:
    print("Room B is already Clean")

print("\nFinal State")
print("Room A =", A)
print("Room B =", B)

print("\nAll rooms are clean.")
