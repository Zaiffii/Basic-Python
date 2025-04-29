array=[0]*15
for i in range(0,15):
    array[i]=int(input(f"Enter Number {i + 1}: "))
for i in range(0,15):
        if array[i] > 0:
            print(f"Your Number: {array[i]} is positive")
        elif array[i] < 0:
            print(f"Your Number: {array[i]} is megative")
        else:
            print(f"Your Number: {array[i]} is zero")
        
        if array[i] % 2 == 0:
            print(f"Your Number: {array[i]} is even")
        else:
            print(f"Your Number: {array[i]} is odd")    