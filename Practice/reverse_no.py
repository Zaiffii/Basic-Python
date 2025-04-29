no=int(input("Enter your number: "))
a=str(no)
length=int(len(a))
i=int=1
quotient=int
remainder=int
reverse=int=0
while i<=length:
    quotient=no//10
    remainder=no%10
    reverse=reverse*10+remainder
    no=quotient
    i+=1
if reverse==a:    
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")         
