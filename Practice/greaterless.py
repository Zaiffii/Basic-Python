no=int(input("Enter any number from 1-100: ")) #Checking if the number is within 1-100
if no>=1 and no<=100:
    if no>50: #greater than condition
        print("Your number is greater than 50")
    elif no<50: #less than condition
        print("Your number is less than 50")
    else: #equal to condition
        print("Your number is equal to 50")
else:
    print("You have entered an invalid number")