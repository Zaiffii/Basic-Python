for n in range(1, 8):
    for i in range(1, n + 1):
        print(" ", end="")
    print("*", end="")
    for j in range(7, n - 1, -1):
        print("  ", end="")
    print("*")

print("        *")
