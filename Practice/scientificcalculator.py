import math
print("Press s for sin, c for cos, t for tan, / for divide, * for multiply, + for addition,\n\
    - for subtraction, p for power, r for square root, m for modulus")
operation=input("Enter operation: ")
#== is used to comapre values and characters need to be are written in ''
if operation=="sin" or operation=='c'or operation=='t':
   angle=int(input("Enter angle in degrees: "))
elif operation=='/'or operation=='*'or operation=='+'or operation=='-':
    number1=int(input("Enter number1: "))
    number2=int(("Enter number2: "))
elif operation=='p': #POWER
        base=int(input("Enter base: "))
        exponent=int(input("Enter exponent: "))
        result=pow(base,exponent)
        print(f"Answer: {result}")
elif operation=='r': #SQUARE ROOT
        number1=int(input("Enter number: "))
        result=math.sqrt(number1)
        print(f"Answer: {result}")
elif operation == 'm':  # Modulus
    number1 = float(input("Enter number 1: "))
    number2 = float(input("Enter number 2: "))
    result = math.fmod(number1, number2)
    print(f"Answer: {result}")
if operation=='/':  #DIVIDE
        result=number1/number2
        print(f"Answer {result}")
elif  operation=='*': #MULTIPLY
        result=number1*number2
        print(f"Answer {result}")
elif operation=='+':  #ADD
        result=number1+number2
        print(f"Answer {result}")
elif operation=='-':  #SUB
        result=number1-number2
        print(f"Answer {result}")
elif operation=='s': #SIN
       result=math.sin(angle)
       print(f"Answer {result}")
elif  operation=='c':  #COS
       result=math.cos(angle)
       print(f"Answer {result}")
elif operation=='t': #TAN
       result=math.tan(angle)
       print(f"Answer {result}")
#if we need to use else then we cannot write a 
#/condition infront of it like operation==tan etc.