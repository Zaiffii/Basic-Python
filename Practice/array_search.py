size=int(input("Enter the size of the list: "))
array=[0]*size
for i in range(0, size):
    array[i] = int(input(f"Enter Number {i + 1}: "))
search=int(input("Enter the element you want to search for: "))
for i in range(0, size):
    if array[i]==search:
        print(f"The eleement you searched for is at index: {i}")