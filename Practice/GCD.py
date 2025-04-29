no1=int(input("Enter your frst number: "))
no2=int(input("Enter your second number: "))
if no1>no2:
    while no2!=0:
     remainder=int=no1%no2
     no1=no2
     no2=remainder
    print(f"Greatest Common Divisor: {no1}")
else:
    while no1!=0:
     remainder=int=no2%no1
     no2=no1
     no1=remainder
    print(f"Greatest Common Divisor: {no2}")
        