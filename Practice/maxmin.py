no1=float(input("Enter your first number: "))
no2=float(input("Enter your second number: "))
no3=float(input("Enter your third number: "))
#Conditions for maximun
if no1>no2 and no1>no3: #First number is maximum
 print(f"{no1} Is maximum and ")
elif no2>no1 and no2>no3: #Second number is maximum
 print(f"{no2} Is maximum and ")
elif no3>no1 and no3>no2: #Third number is maximum
 print(f"{no3} Is maximum and ")    
#Conditions for minimum
if no1<no2 and no1<no3: #First number is minimum
 print(f"{no1} Is miniimum")
elif no2<no1 and no2<no3: #Second number is minimum
 print(f"{no2} Is miniimum")
elif no3<no1 and no3<no2: #Third number is minimum
 print(f"{no3} Is minimum")           
else: #All numbers are equal
 print("All the numbers are equal!")    