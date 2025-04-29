a=int(input("Enter the coefficient of x^2: "))
b=int(input("Enter the coefficient of x: "))
c=int(input("Enter your constant: "))
Disc=int
Disc=(b*b)-(4*a*c) #Formula of discriminat
if Disc>0: #Condition for Real roots
 print("Roots are real!") 
elif Disc==0: #Condition for equal roots
 print("Roots are equal!")
else: #If its not real or equal it will be imaginary
 print("Roots are imaginary")