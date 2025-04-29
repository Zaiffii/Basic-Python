size =10

for i in range(1, size + 1):
    for j in range(1, size + 1):
        if j == i or j == size - i + 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
