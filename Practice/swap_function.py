def swap(no1,no2):
    temp=no1
    no1=no2
    no2=temp
    return no1, no2
no1=int(input("Enter your first number: "))
no2=int(input("Enter your second number: "))
no1, no2=swap(no1,no2)
print(f"number 1: {no1}")
print(f"Number 2: {no2}")