import math
no1=float(input("Enter your first positive integer: "))
no2=float(input("Enter your second positive integer: "))
ans=float
if no1>no2: #if first no is greater than it should be the numerator
  ans=math.fmod(no1,no2) #using modulus to check if this is exactly divisbile or not
  if ans==0:
    print("This is exactly divisible")
  else:
    print("This is not exactly divisible")  
else: #if second no is greater than it should be the numerator
  ans=math.fmod(no2,no1) #using modulus to check if this is exactly divisbile or not
  if ans==0:
    print("This is exactly divisible")
  else:
    print("This is not exactly divisible")   
