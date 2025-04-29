a = eval(input("Enter your quantity for Burgers: "))

b = eval(input("Enter your quantity for Fries: "))

c = eval(input("Enter your quantity for Soda: "))

B=a*5.99
F=b*2.49
S=c*1.99

TotalBurger=B+0.01
TotalFries=F+0.01
TotalSoda=S+0.01

print(f"Menu\n")
print(f"Item\tQuantity\tPrice\tTax\tTotal\n")
print(f"Burger\t{a}\t\t${B}\t$0.01\t${TotalBurger}\n")
print(f"Fries\t{b}\t\t${F}\t$0.01\t${TotalFries}\n")
print(f"Soda\t{c}\t\t${S}\t$0.01\t${TotalSoda}\n")


#python main jab eik hi  print use krna hai multiple lines kay
#liay tou phir har line kay baad\ dalna hai ta kah usko pata chalay
#kah yehi string agli line main continue ho rha hai just like c++