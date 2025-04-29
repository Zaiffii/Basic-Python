i=int
multiply=int=1
for i in range(1,26): #if we do range 0,25 it will strart from 0 0%5 is zero it will store 0 in multiply so any number muitiply by 0 is 0 so the ans will be zero
    result=int=i%5
    if result==0: #if i initialize multiply to 1 here in everyloop it will overwrite the value stored in multiply to 1 
        multiply=multiply*i
print(f"The product of the integers from 1 to 25 which are divisible by 5 is: {multiply}")
