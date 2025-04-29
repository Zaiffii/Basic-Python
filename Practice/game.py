name=input("what is your name? ")
print(f"hey {name} aliens have kidnapped shizuka and you have to accompany Doraemon,Nobita and team to help them rescue shizuka")
print("You have entered the alien's territory, it is extremely  dark out here and we have to rescue shizuka before the aliens wake up MAKE YOUR CHOICE CAREFULLY OR ELSE WE WILL LOOSE SHIZUKA!!")
print("Press 1 to look for shizuka in the boiler room press 2 to look for shizuka in the UFO station press 3 to look for shizuka in the dungeon")
choice=int(input("hint: shizuka is somewhere very dark"))
if choice==1:
    print("chef alien woke up and pushed you in the boiler")
    print("GAME OVER!!")
elif choice==2:
    print("alien's soilder shot you")
    print("GAME OVER!!")
elif choice==3:
    print("you have entered in the dungeon,it is very dark in here, shizuka might be in anywhere in this dungeon, we have to rescue her before the alien wakes up")
    inventory=input("press k to view your inventory")
    if inventory=='k':
        print("press 1: invisiblity cloak")
        print("press 2: night vision glasses")
        print("press 3: sword")
    gadget=int(input("choose one gadget from your inventory"))
    if gadget==1:
        print("invisiblity cloak was of no use here try again later")
    elif gadget==2:
        print("night vision glasses will help you see things clearly in the dark")
        print("shizuka is in cell#4")
        inventory=input("press k to view your inventory")
        if inventory=='k':
            print("press 1: invisiblity cloak")
            print("press 2: sword")
        gadget=int(input("choose one gadget from your inventory"))
        if gadget==1:
            print("it is of no use in this situation, try again later")
        elif gadget==2:
            enemy_health=100
            your_health=100
            while enemy_health>0 and your_health>0:
                print("enemy health= {enemy_health}\nyour health= {your_health}")
                action=input("press f to attack the alien")
                if action=='f':
                   enemy_health=enemy_health-40
                else:
                   your_health=your_health-40
            if your_health==0:
                print("GAME OVER!!")
            else:
                print("alien is dead, yayyy!!")
                print("congragulations for saving shizuka, now you have to get her out of the alien's territory safely")
                inventory=input("press k to view your inventory")
                if inventory=='k':
                   print("press 1: invisiblity cloak")
                gadget=int(input("choose one gadget from your inventory"))
                if gadget==1:
                    print("invisiblity cloak will help you to get shizuka out of alien,s territory easily without them spotting you")
                    print("yayy..you wonn!!")
                else:
                    print("Invalid Gadget")
        else:
            print("Invalid Gadget")               
    elif gadget==3:
        print("sword is of no use try again later")
    else:
        print("Invalid Gadget")    
else:
    print("Please enter a valid choice")       
