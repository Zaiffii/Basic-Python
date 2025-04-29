print("Welcome! Press 1 for Drinks\nPress 2 for Snacks\nPress 3 for Candies") #Menu for products
product=int(input("Enter the product you wish to purchase: ")) 
match product:
    case 1: 
        print("Press 1 for Water (50Rs)\nPress 2 for Soda (100Rs)\nPress 3 for Juice (80Rs)") #Menu for type of drink
        type=int(input("Please select the type of drink you wish to purchase: ")) 
        match type:
           case 1:
              money=float(input("Put 50Rs in the vending machine: ")) #Water
              if money>=50:
                 change=float
                 change=money-50
                 print(f"Your change is Rs.{change}")
                 print("Thank you for using the vending machine")    
              else:
                print("Sorry you have entered an insufficient amount")  
                
           case 2:
              money=float(input("Put 100Rs in the vending machine: ")) #Soda
              if money>=100:
               change=money-100
               print(f"Your change is Rs.{change}")
               print("Thank you for using the vending machine")
              else:
               print("Sorry you have entered an insufficient amount")
                
           case 3: 
               money=float(input("Put 80 Rs in the vending machine: ")) #Juice
               if money>=80:
                change=money-80
                print(f"Your change is Rs.{change}")
                print("Thank you for using the vending machine")
               else:
                print("You have entered an insufficient amount")
           case _:
             print("Invalid choice")

    case 2:
        print("Press 1 for Chips(100Rs)\nPress 2 for Cookies(220Rs)\nPress 3 for Crackers(120Rs)") #Menu for type of snacks
        type=int(input("Please select the type of snacks you wish to purchase: "))
        match type:
           case 1:
              money=float(input("Put 100Rs in the vending machine: ")) #Chips
              if money>=100:
                change=money-100
                print(f"Your change is Rs.{change}")
                print("Thank you for using the vending machine")
              else:
                print("Sorry you have entered an insufficient amount")

           case 2:
               money=float(input("Put 220Rs in the vending machine: ")) #Cookies
               if money>=220:
                change=money-220
                print(f"Your change is Rs.{change}")
                print("Thank you for using the vending machine")
               else:
                print("You have entered an insufficient amount")

           case 3:
               money=float(input("Put 120Rs in the vending machine: ")) #Crackers
               if money>=120:
                change=money-120
                print(f"Your change is Rs.{change}")
                print("Thank you for using the vending machine")
               else:
                print("Sorry you have entered an insufficient amount")

           case _:
             print("Invalid choice")

    case 3:
        print("Press 1 for Chocolate(100Rs)\nPress 2 for Gummy Bears(150Rs)\nPress 3 for Lollipops(120Rs)\n") #Menu for Candies
        type=int(input("Please select the type of candy you wish to purchase: "))
        match type:
           case 1:
               money=float(input("Put 100Rs in the vending machine: ")) #Chocolate
               if money>=100:
                change=money-100
                print(f"Your change is Rs.{change}")
                print("Thank you for using the vending machine")
               else:
                print("Sorry you have entered an insufficient amount")

           case 2:
               money=float(input("Put 150Rs in the vending machine: ")) #Gummy Bears
               if money>=150:
                change=money-150
                print(f"Your change is Rs.{change}")
                print("Thank you for using the vending machine")
               else:
                print("Sorry you have entered an insufficient amount")

           case 3:
               money=float(input("Put 120Rs in the vending machine: ")) #Lollipops
               if money>=120:
                change=money-120
                print(f"Your change is Rs.{change}")
                print("Thank you for using the vending machine")
               else:
                print("Sorry you have entred an in sufficient amount")

           case _:
             print("Invalid choice")

    case _:
     print("Invalid choice")