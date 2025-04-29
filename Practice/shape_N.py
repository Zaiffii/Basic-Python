for i in range(1, 11):
    print("*", end="")
    for j in range(1, 11):
        if j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print("*")
