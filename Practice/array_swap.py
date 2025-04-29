size=int(input("Enter the size of the list: "))
array=[0]*size
for i in range(0, size):
    array[i] = int(input(f"Enter Number {i + 1}: "))
m=array[0]
array[0]=array[size-1]
array[size-1]=m
print(f"After swapping the first value becomes: {array[0]}")
print(f"After swapping the last value becomes: {array[size-1]}")