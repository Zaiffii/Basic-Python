grade=input("Please enter your grade: ") #char is not in python just leave it 
if grade=='A': #In if condition : is used instead of () in python 
    print("Excellent")
elif grade=='B': #Elif is used instead of else if in python
    print("Good")
elif grade=='C': #'A' is used to thell the compiler that it is a character not a constant
    print("Fair")
elif grade=='D':
    print("Poor")
elif grade=='F':
    print("Failure")   
else: #If the user enters any other grade than A,B,C,D,F            
    print("Invalid Grade Please enter the grade from A-F in capital")    