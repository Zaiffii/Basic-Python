def length(name):
    print(len(name))
def word(name):
    count=len(name.split())
    print(f"The number of words are: {count}")
def letter(name):
    for c in name:
        if c.isalpha():
            count+=1
def lower(name):
    print(f"Lower case: {name.lower()}")
def upper(name):
    print(f"Upper case: {name.upper()}")
def change(name):
    for i in range(0,len(name)):
        if name[i].isupper():
            name[i]=name[i].lower()
        elif name[i].islower():
            name[i]=name[i].upper() 
    print(f"Changed name: {name}")          
name=input("Enter your name: ")
print("\tMENU")
print("Press 1 to Calculate length of string")
print("Press 2 to Count number of words in string")
print("Press 3 to Count number of words in string")    
print("Press 4 to Convert a string in lowercase")
print("Press 5 to Convert a string in uppercase")
choice=int(input("What do you want to do: "))
match choice:
    case 1:
        length(name)
    case 2:
        word(name)
    case 3:
        letter(name)
    case 4:
        lower(name)
    case 5:
        upper(name)
    case 6:
        change(name)    
    case _0:
        print("Invalid choice")                    