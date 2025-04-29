array=[0]*10
for i in range(0,10):
    array[i]=int(input(f"Enter Number {i + 1}: "))
largest=array[0]
smallest=array[0]
for i in range(0,10):
    if array[i]>largest:
        largest=array[i];
    if array[i]<smallest:
        smallest=array[i];    
print(f"Largest Value: {largest}")
print(f"Smallest Value: {smallest}")