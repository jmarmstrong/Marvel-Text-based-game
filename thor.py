#thorgamefile
import time
import os
counter = 0
print("Hello you have chosen to play as Thor in this game.")
time.sleep(2)
print("It is a very special day in Asgard, you have been told that you are going to be crowned king tomorrow.")
time.sleep(4)
print("""
1. Accept the news.
2. Deny the news.
""")
choice1 = input("What do you do? ")
if choice1 == "1":
    counter += 1
    print("Congratulations on the honour, Asgard will be happy with its new king.")
    time.sleep(3)
    print("You are travelling to the palace the next day.")
    time.sleep(3)
    print("Suddenly, there is a massive explosion from the palace!!")
    print("""
1. Storm into the palace, ready for a fight.
2. Go and get reinforcements, then storm the palace.
3. Go and get a coffee.
""")
    choice2 = input("What do you do? ")
    if choice2 == "1":
        counter += 1
        print("You draw your sword, burst through the door and...")
        time.sleep(2)
        print("You bellow in rage to see Odin dead, but you don't see the arrow fly from the bow.")
        time.sleep(4)
        print("You die. :( ")
        time.sleep(2)
        print("Please try again.")
        time.sleep(2)
        print("You survived" ,counter, "choices.")
        time.sleep(3)
        again = input("Do you want to play again? ")
        if again == "yes":
            time.sleep(2)
            os.startfile("menu.py")
        if again == "no":
            time.sleep(3)
            exit()
    if choice2 == "2":
        counter += 1
        print("You have arrived at the royal barracks and you have a choice of troops as king. ")
        print("""
1. 60 troops.
2. 40 troops.
3. 20 troops.
""")
        choice3 = input("Which do you choose? ")
        if choice3 == "1":
            counter += 1
            print("All the enemy troops are killed but so are most of your troops. You go for the leader.")
            time.sleep(4)
            print("You kill the enemy leader and you are crowned king of Asgard.")
            time.sleep(3)
            print("Congrats on your victory.")
            print("""
1. Yes
2. No
""")
            print("You survived" ,counter, "choices.")
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
            if again == "no":
                time.sleep(3)
                exit()
        if choice3 == "2":
            counter += 1
            print("You storm the palace but all your troops are killed and your have to face the leader of the army alone.")
            time.sleep(3)
            print("You get stab in the stomach and with your last bit of strength you decapitate the army leader.")
            time.sleep(4)
            print("You have died knowing Asgard is safe.")
            time.sleep(3)
            print("You survived" ,counter, "choices.")
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
            if again == "no":
                time.sleep(3)
                exit()
        if choice3 == "3":
            counter += 1
            print("All your troops are killed and so are you.")
            time.sleep(3)
            print("GAME OVER")
            time.sleep(2)
            print("You survived" ,counter, "choices.")
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menu.py")
            if again == "no":
                time.sleep(3)
                exit()
    if choice2 == "3":
        counter += 1
        print("You enjoy your coffee and grab Mjölnir and your shield.")
        time.sleep(3)
        print("You are just about to burst through the palace door chewing the chocolate cookie you got free with the coffee and...")
        time.sleep(6)
        print("YOU DIE. THE COFFEE WAS POISONED BY DARK ELVES AS REVENGE.")
        time.sleep(4)
        print("At least you have died knowing one good thing...")
        time.sleep(4)
        print("The cookie was really good.")
        time.sleep(4)
        print("You survived" ,counter, "choices.")
        again = input("Do you want to play again? ")
        if again == "yes":
            time.sleep(2)
            os.startfile("menu.py")
        if again == "no":
            time.sleep(3)
            exit()
if choice1 == "2":
    counter += 1
    print("A few hours later you get called to the royal palace and Odin is furious.")
    time.sleep(2)
    print("In his rage Odin tears off your armor and bannishes you to Midgard (Earth).")
    time.sleep(3)
    print("You wake in a field and Mjölnir is no where to be found.")
    time.sleep(2)
    print("You can see two towns in the distance, one to your right and one to your left.")
    print("""
1. Left
2. Right
""")
    choice4 = input("Which way do you go? ")
    if choice4 == "1":
        counter += 1
        print("The town you have chosen is about 4 miles away, it will take you about an hour.")
        time.sleep(4)
        print("You have reached the town and just before you enter a nearby cafe you...")
        time.sleep(4)
        print("You get hit by a car.")
        time.sleep(2)
        print("The person that hit in their car offers you their help.")
        time.sleep(1)
        print("""
1. Accept their help.
2. Ignore them and go get a coffee. (Cookie free with a large coffee.)
""")
        choice5 = input("What do you do? ")
        if choice5 == "1":
            counter += 1
            print("You have got in the car and you go with the person further into the town.")
            time.sleep(3)
            print("The person has taken you to what looks like a lab on the other side of the town.")
            time.sleep(3)
            print("Suddenly realising you don't know the person name, you ask for the person's name.")
            time.sleep(3)
            print("The person replies, I'm Jane Foster.")
            time.sleep(2)
            print("Jane asks you your name.")
            time.sleep(3)
            print("""
1. Thor, son of Odin.
2. Donald Blake.
""")
            choice6 = input("What do you tell her? ")
            if choice6 == "1":
                counter += 1
                print("You have told Jane your real name and she suggests that you should take the name, Donald Blake.")
                time.sleep(5)
                print("You accept the name and follow Jane into the lab.")
                time.sleep(3)
                print("Here Jane shows you her work and explains to you what it means.")
                time.sleep(3)
                print("While Jane goes to make a phone call, you are reading about voids and nebulas not taking in a word when two men storm through the door.")
                time.sleep(6)
                print("Their sudden appearance startles you and you jump up ready for a fight.")
                time.sleep(3)
                print("But the men just stand there and look at you.")
                time.sleep(3)
                print("Then they advance and something hits you in the back of the head.")
                time.sleep(3)
                print("You have been shot.")
                time.sleep(3)
                print("You have died.")
                time.sleep(3)
                print("You survived" ,counter, "choices.")
                again = input("Do you want to play again? ")
                if again == "yes":
                    time.sleep(2)
                    os.startfile("menu.py")
                if again == "no":
                    time.sleep(3)
                    exit()
            if choice6 == "2":
                counter += 1
                print("Jane says that she likes that name and that it was the name of her ex.")
                time.sleep(3)
                print("Two people come out from what looks like the kitchen and they ask Jane what your name is.")
                time.sleep(4)
                print("Jane tells them your name and that the two people are called Darcy Lewis and Erik Selvig.")
                time.sleep(5)
                print("You tell the three people that you have to find Mjölnir.")
                time.sleep(2)
                print("Jane, Darcy and Erik look at you like your mad.")
                time.sleep(2)
                print("You explain about Mjölnir and about Asgard.")
                time.sleep(2)
                print("Jane says that when you landed there was another explosion 3 miles away.")
                time.sleep(2)
                print("You ask if you can go to the crash site and get Mjölnir.")
                time.sleep(2)
                print("Jane agrees but before you leave she suggests you put on something more suited to Earth.")
                time.sleep(2)
                print("You change out of your Asgardian robes and into a t-shirt and jeans.")
                time.sleep(2)
                print("After you have changed you set out in the car to the crash site.")
                time.sleep(2)
                print("While on the way the crash site it starts to rain.")
                time.sleep(2)
                print("You have arrived at the site and it is swarming with SHIELD agents.")
                time.sleep(3)
                print("""
1. Storm in and mow down anyone in your path.
2. Stay where you are and strategize.
""")
                choice7 = input("What do you do.")
                if choice7 == "2":
                    counter += 1
                    print("You look around the area and how hard this is going to be hits you.")
                    time.sleep(4)
                    print("But thats not the only thing that hits you, something hard to the back of the head.")
                    time.sleep(5)
                    print("You have died. Nice try.")
                    time.sleep(3)
                    print("You survived" ,counter, "choices.")
                    again = input("Do you want to play again? ")
                    if again == "yes":
                        time.sleep(2)
                        os.startfile("menu.py")
                    if again == "no":
                        exit()
                if choice7 == "1":
                    counter += 1
                    print("You jump out the car and run full pelt smashing through the door.")
                    time.sleep(3)
                    print("You take down 1, 2, 3 guys while running down a corridor and see 6 more armed agents.")
                    time.sleep(3)
                    print("""
1. Run at them and hope for the best.
2. Turn around and try another route.
""")
                    choice9 = input("What do you do?")
                    if choice9 == "2":
                        counter += 1
                        print("You turn around and run back up the corridor.")
                        time.sleep(3)
                        print("You round the corner and there is a sudden sound like a gun shot.")
                        time.sleep(3)
                        print("You have been shot. :(")
                        time.sleep(3)
                        print("You have died. Nice try.")
                        time.sleep(3)
                        print("You survived" ,counter, "choices.")
                        again = input("Do you want to play again? ")
                        if again == "yes":
                            time.sleep(2)
                            os.startfile("menu.py")
                        if again == "no":
                            exit()
                    if choice9 == "1":
                        counter += 1
                        print("You take down all six in a couple of seconds and race through the door.") 
                        time.sleep(3)
                        print("You see Mjölnir and go to take it.")
                        time.sleep(2)
                        print("You pull, nothing happens. You pull harder, nothing happens.")
                        time.sleep(3)
                        print("You know something is wrong.")
                        time.sleep(3)
                        print("Two people grab you under the arms and pull you away from your hammer.")
                        time.sleep(3)
                        print("They take you to a room where Jane is waiting.")
                        time.sleep(3)
                        print("Jane takes you back to the lab and you stay the night.")
                        time.sleep(3)
                        print("You wake up to an loud explosion.")
                        time.sleep(2)
                        print("""
1. Yes
2. No
""")
                        choice10 = input("Do you investigate? ")
                        if choice10 == "2":
                            counter += 1
                            print("You decide that this noise is not worth your time and you fall asleep again.")
                            time.sleep(5)
                            print("You don't notice the sharp pain in the middle of your chest")
                            time.sleep(4)
                            print("The last thing you remember is a strong smell of coffee.")
                            time.sleep(4)
                            print("You have been stabed.")
                            time.sleep(2)
                            print("You have died. Nice try.")
                            time.sleep(3)
                            print("You survived" ,counter, "choices.")
                            again = input("Do you want to play again? ")
                            if again == "yes":
                                time.sleep(2)
                                os.startfile("menu.py")
                            if again == "no":
                                exit()
                        if choice10 == "1":
                            counter += 1
                            print("You burst through the hall door with your shirt on backwards and onto the street.")
                            time.sleep(4)
                            print("You turn and see the destroyer tearing up the coffee shop.")
                            time.sleep(3)
                            print("You pick up a metal rod and impale the destroyer through the back.")
                            time.sleep(3)
                            print("The destroyer turns around it's head grabs you and throws you across the road.")
                            time.sleep(4)
                            print("You grab a bin lid and chuck it at the destroyer.")
                            time.sleep(3)
                            print("The destroyer turns around and yells YOU ARE NOT WORTHY!!!!")
                            time.sleep(3)
                            print("You run at the destroyer and a pure energy beam hits you in the chest.")
                            time.sleep(3)
                            print("You get thrown back and go through the post office window.")
                            time.sleep(3)
                            print("You climb out of the wreckage and stop due to a whistling.")
                            time.sleep(3)
                            print("You turn around just in time to see Mjölnir flying towards.")
                            time.sleep(3)
                            print("You stretch out your hand, hope for the best and catch it.")
                            time.sleep(3)
                            print("The destroyer stops to look at you holding Mjölnir.")
                            time.sleep(3)
                            print("Your Asgardian armour flows over your skin and you hurl your hammer at the destroyer.")
                            time.sleep(3)
                            print("You call back Mjölnir and throw it back at the destroyer")
                            time.sleep(3)
                            print("The hammer goes through the destroyer's chest.")
                            time.sleep(3)
                            print("You strike the destroyer with lightning and it explodes.")
                            time.sleep(3)
                            print("You are congratulated for the work you have done and are allowed back into Asgard.")
                            time.sleep(3)
                            print("You tell Jane you have to leave but you will be back.")
                            time.sleep(3)
                            print("You open the Bifrost and return to Asgard.")
                            time.sleep(3)
                            print("You fly down the rainbow bridge and into the palace and see Loki on the throne.")
                            time.sleep(3)
                            print("""
1. Get angry with him.
2. Go get a coffee and then get angry with him.
""")
                            choice11 = ("What do you do? ")
                            if choice11 == "2":
                                counter += 1
                                print("You quickly run to the coffee shop and then return.")
                                time.sleep(4)
                                print("You pull open the palace doors and the blade of Loki's sceptre is plunged into your chest.")
                                time.sleep(5)
                                print("You have died. Nice try.")
                                time.sleep(3)
                                print("You survived" ,counter, "choices.")
                                again = input("Do you want to play again? ")
                                if again == "yes":
                                    time.sleep(2)
                                    os.startfile("menu.py")
                                if again == "no":
                                    exit()
                                
                            if choice11 == "1":
                                counter += 1
                                print("You grab him and hurl him through the palace doors.")
                                time.sleep(3)
                                print("You fly loki to the rainbow brigde and place him down with Mjölnir on his chest.")
                                time.sleep(3)
                                print("You shout at loki about you thought Odin was dead and Loki tells you that the frost giants are coming.")
                                time.sleep(4)
                                print("You think fast and decide to break the rainbow brigde to stop the giants.")
                                time.sleep(3)
                                print("Loki yells for you to stop but with one last strike your hammer goes through the brigde")
                                time.sleep(3)
                                print("You and Loki are pulled over the edge and you are holding loki from the infinite abyss.")
                                time.sleep(3)
                                print("You start to lift loki up to the edge but then suddenly... he lets go.")
                                time.sleep(3)
                                print("You have completed the game. Well done!!")
                                time.sleep(3)
                                print("You survived" ,counter, "choices.")
                                again = input("Do you want to play again? ")
                                if again == "yes":
                                    time.sleep(2)
                                    os.startfile("menu.py")
                                if again == "no":
                                    time.sleep(3)
                                    exit()
        if choice5 == "2":
            counter += 1
            print("You enter the cafe and order a large coffee and drink it while eating your cookie.")
            time.sleep(2)
            print("You have finished your coffee and cookie to your surprise the person that hit you with their car is still waiting outside looking expectant.")
            time.sleep(5)
            print("Finally you give in and get in the car.")
            time.sleep(2)
            print("The person takes you further into town.")
            time.sleep(3)
            print("The person has taken you to what looks like a lab on the other side of the town.")
            time.sleep(3)
            print("Suddenly realising you don't know the person name, you ask for the person's name.")
            time.sleep(3)
            print("The person replies, I'm Jane Foster.")
            time.sleep(2)
            print("Jane asks you your name.")
            print("""
1. Thor, son of Odin.
2. Donald Blake.
""")
            choice8 = input("What do you tell her? ")
            if choice8 == "1":
                counter += 1
                print("You have told Jane your real name and she suggests that you should take the name Donald Blake.")
                time.sleep(5)
                print("You accept the name and follow jane into the lab.")
                time.sleep(3)
                print("Here Jane shows you her work and explains to you what it means.")
                time.sleep(3)
                print("While Jane goes to make a phone call, you are reading about voids and nebulas not taking in a word when two men storm through the door.")
                time.sleep(6)
                print("Their sudden apperance startels you and you jump up ready for a fight.")
                time.sleep(3)
                print("But the men just stand there and look at you.")
                time.sleep(3)
                print("Then they advance and something hits you in the back of the head.")
                time.sleep(3)
                print("You have been shot.")
                time.sleep(3)
                print("You have died.")
                time.sleep(3)
                print("You survived" ,counter, "choices.")
                again = input("Do you want to play again? ")
                if again == "yes":
                    time.sleep(2)
                    os.startfile("menu.py")
                if again == "no":
                    time.sleep(3)
                    exit()
            if choice8 == "2":
                counter += 1
                print("Here Jane shows you her work and explains to you what it means.")
                time.sleep(3)
                print("While Jane goes to make a phone call, you are reading about voids and nebulas not taking in a word when two men storm through the door.")
                time.sleep(7)
                print("Their sudden apperance startels you and you jump up ready for a fight.")
                time.sleep(3)
                print("But the men just stand there and look at you.")
                time.sleep(3)
                print("Then they advance and something hits you in the back of the head.")
                time.sleep(3)
                print("You have been shot.")
                time.sleep(3)
                print("You have died.")
                time.sleep(3)
                print("You survived" ,counter, "choices.")
                again = input("Do you want to play again? ")
                if again == "yes":
                    time.sleep(2)
                    os.startfile("menu.py")
                if again == "no":
                    time.sleep(3)
                    exit()
    if choice4 == "2":
        counter += 1
        print("The town you have chosen is about 3 miles away, it will take you about 45 minutes.")
        time.sleep(3)
        print("You reach the town and something doesn't feel right.")
        time.sleep(2)
        print("It's very quiet and the town seemed deserted.")
        time.sleep(3)
        print("Suddennly there is a loud crash, you whip around and there is a man standing with a gun...")
        time.sleep(4)
        print("Without warning he pulls the trigger.")
        time.sleep(3)
        print("There was nothing you could have done. You are dead.")
        time.sleep(3)
        print("You survived" ,counter, "choices.")
        again = input("Do you want to play again???? ")
        if again == "yes":
            time.sleep(2)
            os.startfile("menu.py")
        if again == "no":
            time.sleep(3)
            exit() 
