print("          *")
for n in range(1, 11):
    for i in range(10, n, -1):
        print(" ", end="")
    print("*", end="")
    
    for j in range(1, n * 2 + 1):
        if n == 5:
            print("*", end="")
        else:
            print(" ", end="")
    print("*")
