no1=int(input("Enter your first number: "))
no2=int(input("Enter your second number: "))
a=int=no1
b=int=no2
if no1>no2:
    while no2!=0:
        remainder=int=no1%no2
        no1=no2
        no2=remainder
    GCD=int=no1
    LCM=int=(a*b)/GCD #the values of no1 & no2 are changed for the calculation of GCD in the forumula of LCM the multiplication of original no1&no2 is required
    print(f"Least Common Multiplier: {LCM}")
else:
    while no1!=0:
        remainder=int=no2%no1
        no2=no1
        no1=remainder
    GCD=int=no2
    LCM=int=(a*b)/GCD #the values of no1 & no2 are changed for the calculation of GCD in the forumula of LCM the multiplication of original no1&no2 is required
    print(f"Least Common Multiplier: {LCM}")