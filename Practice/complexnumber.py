import math
print("Press * for multiply, + for addition, - for subtraction, i for increment,\n\
   d for decrement, m for modulus")
operation=input("Enter your operation:" )
if operation=='i' or operation=='d':
    Rz1=int(input("Enter your real part of 1st complex number:") )
    Im1=int(input("Enter your imaginary part of 1st complex number: "))
else:
    Rz1=int(input("Enter your real part of 1st complex number:" ))
    Im1=int(input("Enter your imaginary part of 1st complex number:" ))
    Rz2=int(input("Enter your real part of 2nd complex number:" ))
    Im2=int(input("Enter your imaginary part of 2nd complex number:" ))   
if operation=='*':#MULTIPLY
    Rz=Rz1*Rz2 - Im1*Im2
    Im=Rz1*Im2 + Im1*Rz2
    print(f"{Rz}+{Im}i")
elif operation=='+':#ADD
    Rz=Rz1+Rz2
    Im=Im1+Im2
    print(f"{Rz}+{Im}i")
elif operation=='-':#SUBTRACT
    Rz=Rz1-Rz2
    Im=Im1-Im2
    print(f"{Rz}"+"{Im}i")
elif operation=='i':#INCREMENT
    Rz1+=1
    Im1+=Im1
    print(f"{Rz1}+{Im1}i")
elif operation=='d':#DECREMENT
    Rz1+=1
    Im1-=1
    print(f"{Rz1}+{Im1}i")
elif operation == 'm':#MODULUS
    modulus1 = math.sqrt(Rz1**2 + Im1**2)
    modulus2 = math.sqrt(Rz2**2 + Im2**2)
    print(f"Modulus of the first complex number: {modulus1}")
    print(f"Modulus of the second complex number: {modulus2}")
    