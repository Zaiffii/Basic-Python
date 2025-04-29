for N in range(1, 21):
    print("*", end="")  # Print first line
print()

for N in range(1, 11):
    for i in range(20, N * 2, -1):
        print(" ", end="")
    print("*")  # Print the star after spaces

for N in range(1, 21):
    print("*", end="")  # Print last line
