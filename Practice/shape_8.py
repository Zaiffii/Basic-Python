for n in range(1, 8):
    print("*", end="")
print()

for n in range(1, 8):
    print("*", end="")
    for j in range(1, 6):
        if n == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print("*")

for n in range(1, 8):
    print("*", end="")
