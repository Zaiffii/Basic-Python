while True:
    i = 1
    j = 1
    no = int(input("Enter the number for which you want the multiplication table of: "))
    if no > 0:
        for i in range(1, 11):
            result = no * i
            while j == i:
                print(f"{no} x {i} = {result}")
                j += 1
    else:
        print("Please enter a positive number.")

    # Asking the user if they want to continue
    choice = input("Do you want to print a multiplication table for another number? (yes/no): ").lower()
    if choice != "yes":
        print("Goodbye!")
        break  # Exit the loop if the user doesn't want to continue
