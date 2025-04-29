while True:
    # Input the number of rows for the pyramid
    rows = int(input("Enter the number of rows for the Fibonacci pyramid: "))

    # Initialize the first two numbers of the Fibonacci sequence
    a, b = 0, 1
    count = 0  # Track how many Fibonacci numbers are printed

    for i in range(1, rows + 1):  # Loop for each row
        # Print leading spaces for alignment
        print("   " * (rows - i), end="")

        # Print Fibonacci numbers for the current row
        for j in range(i):
            if count == 0:
                next_fib = a
            elif count == 1:
                next_fib = b
            else:
                next_fib = a + b
                a, b = b, next_fib

            # Print the number with fixed spacing
            print(next_fib, end=" ")
            count += 1

        print()  # Move to the next line after each row

    # Ask if the user wants to generate another pattern
    choice = input("Do you want to generate another pattern? (y/n): ").strip().lower()
    if choice != 'y':
        break