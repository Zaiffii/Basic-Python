no=int(input("Enter your number: "))
i=int
Fa=int=1 
Fb=int=1
Ans=int
a=int
b=int
if no==1:
    print("F1=1")
elif no==2:
    print("F2=1")
else:
    for i in range(3,no+1):
        Ans=Fa+Fb
        a=Fa
        b=Fb
        Fa=Fb #Here if I write Fb=Ans then write Fa=Fb then the value of Fb would already by overwritten by ans so the value of Fa would also be over written by ans instead of Fb
        Fb=Ans
              #If we write a=Fa & b=Fb then the value of Fa is replaced by Fb and value of Fb is replaced by Ans which is not correct
    print(f"F{no}=F{no-1}+F{no-2}={a}+{b}={Ans}")
#We used a & b just to print in the correct order otherwise there is no use of a&b.
#If we write print(f"F{no}=F{no-1}+F{no-2}={Fa}+{Fb}={Ans}") it would not be correct because in the loop the value of Fa is replaced by Fb and the value of Fb is replace by Ans            