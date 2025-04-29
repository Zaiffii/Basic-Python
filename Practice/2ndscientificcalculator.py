import math   
print("Welcome! Press 1 for Arithmetic Operations (Addition, Subtraction, Multiplication, Division)\nPress 2 for Trignometric Operations (Sine, Cosine, Tangent)\nPress 3 for Exponential & Logarithmic Operations (Power, Logarithm)") #Menu for operations
operation=int(input("Please Enter the operation that you want to perform: "))
match operation:
      case 1:
          print("Press 1 for division(/)\nPress 2 for multiplication(*)\nPress 3 for addition(+)\nPress 4 for subtraction(-)") #Menu for arithmetic operations
          type=int(input("Please enter the type of arithmetic operation that you want to perform: "))
          no1=float(input("Please enter your first number: "))
          no2=float(input("Please enter your second number: "))
          match type: 
                case 1: #Divide
                 match int(no2):
                        case 0:
                           print("division by 0 is not possible")
                        
                        case _:
                         result=no1/no2
                         print(f"Answer: {result}")      
                
                case 2:  #Multiply
                 result=no1*no2
                 print(f"Answer: {result}")

                case 3:  #PLus
                 result=no1+no2
                 print(f"Answer: {result}")

                case 4:  #Subtract
                 result=no1-no2
                 print(f"Answer: {result}")

                case _:
                 print("You have entered an invalid type of arithmetic operation")

      case 2:
          print("Press 1 for sine\nPress 2 for cosine\nPress 3 for tangent") #Menu for trigonometric operations
          type=int(input("Please enter the type of Trigonometric Operation that you want to perform: "))
          angle=int(input("Please enter your angle in radians: "))
          match type:           
               case 1:
                  result=math.sin(angle) #Sine
                  print(f"Answer: {result}")

               case 2:
                  result=math.cos(angle); #Cosine
                  print(f"Answer: {result}")

               case 3:
                  result=math.tan(angle) #Tangent
                  print(f"Answer: {result}")

               case _:
                print("You have entered an invalid type of trigonometric operation")      

      case 3:
          print("Press 1 for Power function\nPress 2 for natural Logarithim function") #Functions
          type=int(input("Enter the type of function that you want to perform: "))
          no1=float(input("Enter your base: "))
          match type:
               case 1:
                  no2=float(input("Enter your exponent: ")) 
                  result=math.pow(no1,no2) #Power
                  print(f"Answer: {result}")

               case 2:
                  result=math.log(no1) #Log 
                  print(f"Answer: {result}")

               case _:
                print("You have entered an invalid type of Power or logarithmic function")             
      case _:
       print("Invalid Operation")