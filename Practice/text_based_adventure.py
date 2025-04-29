name=input("Please enter your name:")
print(f"Hey! {name} Your friends are Ron and Hermione. You three are sitting in the Gryfindor lobby thinking about how to stop Voldemort")
print("You have told Professor McGonagall that you have a doubt that Professor Snape is with Voldemort and is trying to steal the Philosophers Stone")
print("But Professor McGonagall has told you that there is nothing like that and Professor Snape is the one helping to protect the stone and you should go in your rooms")
firstchoice=int(input("You have 2 options you can press 1 to go to your rooms and leave it or You can press 2 stop it by yourself. What are your going to do? "))
if firstchoice==1:
    print("Lord Voldemort has returened and is very powerful your life is in danger!!! GameOver :/ Run it again to Try again!")
elif firstchoice==2:
    print("You along with Hermione and Ron have gathered in the Gryffindor common room after 12 o clock. You are pretty sure that everyone has slept and now you can finally")
    print("investigate the situation.")
    print("You see that your friend Neville is standing in your way and is not letting you pass through because he is afraid that you guys might get into trouble")
    Neville=input("You have 2 options you can type Absornious to cast a spell on him which will make him go to sleep or you can type tell to tell him everything in detail and hope that he will let you go")
    if Neville=="Absornious" or Neville=="absornious":
        print("You take out your wand and cast a spell named Absornious to make Neville go to sleep.") 
        inventory=input("You can view your inventory by pressing i")
        if inventory=='i':
            print("\tInventoryWand")
        print("You guys go to the third floor there are three doors.")
        print("Door 1 is in the north type  gonorth to go to that door, Door 2 is in the east type goeast to go to that door, Door 3 is in the west type gowest to go to that door")
        print("There is a talking picture with a riddle if you can solve it you can know which door is the right one")
        thirdfloor=input("The Riddle is that: I am the direction where the compass always points, guiding explorers through snowy joints. I am home to the pole that is icy and cold. What am I?: ")
        if thirdfloor=="gonorth":
            print("There is a talking picture besides a door you need to answer a riddle in order to unlock that door")
            secondriddle=input("The riddle is that: I am tall when I am young, and I am short when I am old. What am I?: ")
            if secondriddle=="candle" or secondriddle=="Candle":
                print(f"Nice thinking {name} Congratulations you have entered the room, There is a three headed dog with its paw on a basement door if you come close you will get eaten")
                threeheadeddog=input("You see a potion that can make it paralize for 1 hour type Use to use it or Miss to miss it: ")
                if threeheadeddog=="Use" or threeheadeddog=="use":
                    print("You used the portion to paralize the dog.") 
                    print("Potion has been added to your inventory Press i to view it")
                    inventory=input
                    if inventory=='i':
                        print("\tInventoryWand\tPotion")
                    print("All three of you jumped into the basement you are caught by the plant named Aconitum it is killing all of you by trapping you tight")
                    print("with its roots Your friend Hermione is saying that she read about it somewhere if you guys relax it will leave you after that both Hermione and Ron are vanished.")
                    Aconitum=input("You can either trust Hermione and type Relax to relax or you can type Struggle to struggle so that you can grap your want and do something.  Now what will you do?: ")
                    if Aconitum=="Relax" or Aconitum=="relax":
                        print("Yay Good to know that you trust your friends!")
                        print("There was a door to the next room as soon as you entered that room three men are there they casted a spell named crucio on you")
                        Threemen=input("Your health dropped to 70%, You can either type Surrender or type Fight: ")
                        if Threemen=="Surrender" or Threemen=="surrender":
                            print("They stil tortured you untill all of you died")
                        elif Threemen=="Fight" or Threemen=="fight":
                            print("You guys grapped your wand and you can now make a counter spell you have two options since it is the first year you dont know many fighting spells")
                            spell=input("You can either use Expelliarmus or the same spell that they used that is crucio. What would it be?: ")
                            if spell=="Expelliarmus" or spell=="Expelliarmus":
                                print("Nice choice since Expelliarmus is a much powerful spell than Crucio")
                                enemyhealth=80 
                                yourhealth=70
                                while enemyhealth>0 and yourhealth>0:
                                    print(f"Your health= {yourhealth}")
                                    print(f"Enemy Health= {enemyhealth}")
                                    fight=input("Type Expelliarmus again to fight again Hurry!! ")
                                    if fight=="Expelliarmus" or fight=="Expelliarmus":
                                        print("Clang! Dshhhh! Smack! Whack! Dshhhh! Dshhhh! Whack! ")
                                        enemyhealth=enemyhealth-20
                                    else:
                                        yourhealth=yourhealth-10
                                        print("Clang! Dshhhh! Smack! Whack! Dshhhh! Dshhhh! Whack! ")
                                if yourhealth==0:
                                    print("The enemy has killed you :/ Better luck next time! Run it again to Try again")
                                else:
                                    print(f"Congratualtions you have defeated the enemy. Your health is :{yourhealth}")
                                    print("The enemy which Ron was dealing with threw a knife at Ron which hit him in the stomach now you have to make a difficult choice Either you can type Back to take Ron to the hospital with Hermione")
                                    difficultchoice=input("or you can type Forward to carry on to defeat Voldemort from returning and protect the Philosophers Stone. So what is to gonna be?: ")
                                    if difficultchoice=="Back" or difficultchoice=="back":
                                        print("You made the wRong choice. NO DOUBT we should stay with friends when they need us but sometimes we need to think about other people also if Voldemort returns he will kill")
                                        print("innocent people and Hermione could take Ron. Dont be sad it was indeed a very hard choice to make. GameOver :/ Run it again to Try again!")  
                                    elif difficultchoice=="Forward" or difficultchoice=="forward":
                                        print(f"Excellent choice {name} You have got to stop Voldemort now. There is the last door with another riddle. Behind that door you are quite sure that Snape is stealing Philosophers Stone")
                                        thirdriddle=input("The riddle is that: Iam always infront of you but cannot be seen what am I?: ")
                                        if thirdriddle=="Future" or thirdriddle=="future":
                                            print(f"Execellent Guess {name} No doubt why you are the CHOSEN ONE!")
                                            print("When you entered the room you saw that Instead of Snape your favourite Professor Quirell is standing and behind his head there is the face of Voldemort")
                                            print("He shouts at you and demands to give him the Philosophers Stone. You are confused because you dont have the Philosophers Stone but you feel that something is present in the left pocket of your jeans")
                                            print("When you take it out you see that it is the Philosophers Stone.")
                                            inventory=input("Press i to view your inventory")
                                            if inventory=='i':
                                                print("\tInventoryWand\tPotion\tPhilosophers Stone")
                                            print("You read that it can give you powers. Quirell comes at you and pushes you")
                                            quirell=input("You can either type fight to fight with him or you can type leave to give up and let him take the Philosophers Stone. What will you do?: ")
                                            if quirell=="Leave" or quirell=="leave":
                                                print("Wrong choice after all the efforts you should have tried your best to stop him and should not have given up your hope GameOver :/ Run it again to Try again!")
                                            elif quirell=="Fight" or quirell=="fight":
                                                print("You went to stop him when you grabbed him by your hands to stop him his skin started burning You both are confused what just happened")
                                                quirellhealth=80
                                                while quirellhealth != 0 and yourhealth !=0:
                                                    print(f"Yourhealth = {yourhealth}")
                                                    print(f"Quirell health = {quirellhealth}")
                                                    finalfight=input("Type Attack to try putting hands on him again so that he can burn: ")
                                                    if finalfight=="Attack" or finalfight=="attack":
                                                        quirellhealth=quirellhealth-20
                                                        print("Hiss!Hiss!Hiss!Hiss!Hiss!Hiss!Hiss!Hiss!Hiss!Hiss!Hiss!Hiss!Hiss!")
                                                        print("Ughhhhhh quirell shouting in pain")
                                                    else:
                                                        print("Quirell hits you")
                                                        yourhealth=yourhealth-10
                                                        print(f"{name} Shouting in pain")
                                                if yourhealth==0:
                                                        print("Quirell killed you :/ Game Over Better luck next time Run it again to Try again!")
                                                else:
                                                    print("You have finally killed quirell and stopped Voldemort from returining!!!")
                                                    print("You passed out and have woken up in the Hogwarts Hospital Ron and Hermione are sleeping on the sofa")
                                                    print("Dumbeldore comes and Congratulates you on your bravery!!")
                                                    print("\tHAPPY ENDING")
                                                    print(f"Well done {name} We need more Wizards like you :-)")
                                                    print("See you again in the next chapter!!!")
                                            else:
                                                print("Please enter a valid move")
                                        else:
                                            print("Oops wRong guess try again")    
                                    else:
                                        print("Please type a valid choice")
                            elif spell=="Crucio" or spell=="crucio":
                                    print("Since you used crucio so your health and the health of the enemy is being decreased at the same time")
                                    print("Your health was already dropped at 70% because they made the first attack and their health is at 100% so you will die eventually GameOver :/ Run it again to Try again!")
                            else:
                                    print("Please type a valid spell")
                        else:
                            print("Please type a valid move")
                    elif Aconitum=="Struggle" or Aconitum=="struggle":
                        print("You could not grap your want because when you struggled the plant grapped you more firmly and squished you, You should learn to trust your friends GameOver :/ Run it again to Try again!")
                    else:
                        print("Please type a valid move")
                elif threeheadeddog=="Miss" or threeheadeddog=="miss":
                    print("The dog woke up and killed all of you by ripping you off in several pieces, Better luck next time Run it again to Try again!")
                else:
                    print("Please type a valid move")
            else:
                print("Nope try again")
        elif thirdfloor=="goeast":
                print("You chose to go to door:2 there were 2 teachers there you got caught and are in detention now Oops better luck next time!! Run it again to Try again!")
        elif thirdfloor=="gowest":
            print("You chose to go to door:3 there was a ditch you all fell in that and died Game over :/ Run it again to Try again!")  
        else:
            print("Please type a valid direction")
    elif Neville=="Tell" or Neville=="tell":
        print("Neville doesn't understand it & he don't let you leave either.GameOver :/ Run it again to Try again!")
    else:
        print("Please type a valid spell")   
else:
    print("Please enter a valid choice")
