age=int(input("Please enter your age: "))
if age<18: #Condition for child
 print("CHILD")
elif age>=18 and age<35: #Condition for adult
 print("ADULT")
else: #If it's not child nor adult then it must be senior
 print("SENIOR") 