#thorgamefile
import time
import os
def pp (text,pause):
    print(text)
    time.sleep(pause)
def po (pause,openfile):
    time.sleep(pause)
    os.startfile(openfile)
counter = 0
pp("Hello you have chosen to play as Thor in this game.",2)
pp("It is a very special day in Asgard, you have been told that you are going to be crowned king tomorrow.",4)
pp("""
1. Accept the news.
2. Deny the news.
""",2)
choice1 = input("What do you do?:")
if choice1 == "1":
    counter += 1
    pp("Congratulations on the honour, Asgard will be happy with its new king.",3)
    pp("You are travelling to the palace the next day.",3)
    pp("Suddenly, there is a massive explosion from the palace!!",1)
    pp("""
1. Storm into the palace, ready for a fight.
2. Go and get reinforcements, then storm the palace.
3. Go and get a coffee.
""",1)
    choice2 = input("What do you do?:")
    if choice2 == "1":
        counter += 1
        pp("You draw your sword, burst through the door and...",2)
        pp("You bellow in rage to see Odin dead, but you don't see the arrow fly from the bow.",4)
        pp("You die. :( ",2)
        pp("Please try again.",2)
        pp("You survived" ,counter, "choices.",3)
        again = input("Do you want to play again?:")
        if again == "yes":
            po(2,menu.py)
        if again == "no":
            time.sleep(3)
            exit()
    if choice2 == "2":
        counter += 1
        pp("You have arrived at the royal barracks and you have a choice of troops as king. ",1)
        pp("""
1. 60 troops.
2. 40 troops.
3. 20 troops.
""",1)
        choice3 = input("Which do you choose?:")
        if choice3 == "1":
            counter += 1
            pp("All the enemy troops are killed but so are most of your troops. You go for the leader.",4)
            pp("You kill the enemy leader and you are crowned king of Asgard.",3)
            pp("Congrats on your victory.",1)
            pp("""
1. Yes
2. No
""",1)
            pp("You survived" ,counter, "choices.",1)
            again = input("Do you want to play again?:")
            if again == "yes":
                po(2,menu.py)
            if again == "no":
                time.sleep(3)
                exit()
        if choice3 == "2":
            counter += 1
            pp("You storm the palace but all your troops are killed and your have to face the leader of the army alone.",3)
            pp("You get stab in the stomach and with your last bit of strength you decapitate the army leader.",4)
            pp("You have died knowing Asgard is safe.",3)
            pp("You survived" ,counter, "choices.",1)
            again = input("Do you want to play again?:")
            if again == "yes":
                po(2,menu.py)
            if again == "no":
                time.sleep(3)
                exit()
        if choice3 == "3":
            counter += 1
            pp("All your troops are killed and so are you.",3)
            pp("GAME OVER",2)
            pp("You survived" ,counter, "choices.",2)
            again = input("Do you want to play again?:")
            if again == "yes":
                po(2,menu.py)
            if again == "no":
                time.sleep(3)
                exit()
    if choice2 == "3":
        counter += 1
        pp("You enjoy your coffee and grab Mjölnir and your shield.",3)
        pp("You are just about to burst through the palace door chewing the chocolate cookie you got free with the coffee and...",6)
        pp("YOU DIE. THE COFFEE WAS POISONED BY DARK ELVES AS REVENGE.",4)
        pp("At least you have died knowing one good thing...",4)
        pp("The cookie was really good.",4)
        pp("You survived" ,counter, "choices.",1)
        again = input("Do you want to play again?:")
        if again == "yes":
            po(2,menu.py)
        if again == "no":
            time.sleep(3)
            exit()
if choice1 == "2":
    counter += 1
    pp("A few hours later you get called to the royal palace and Odin is furious.",2)
    pp("In his rage Odin tears off your armor and bannishes you to Midgard (Earth).",3)
    pp("You wake in a field and Mjölnir is no where to be found.",2)
    pp("You can see two towns in the distance, one to your right and one to your left.",1)
    pp("""
1. Left
2. Right
""",1)
    choice4 = input("Which way do you go?:")
    if choice4 == "1":
        counter += 1
        pp("The town you have chosen is about 4 miles away, it will take you about an hour.",4)
        pp("You have reached the town and just before you enter a nearby cafe you...",4
        pp("You get hit by a car.",2)
        pp("The person that hit in their car offers you their help.",1)
        pp("""
1. Accept their help.
2. Ignore them and go get a coffee. (Cookie free with a large coffee.)
""",1)
        choice5 = input("What do you do?:")
        if choice5 == "1":
            counter += 1
            pp("You have got in the car and you go with the person further into the town.",3)
            pp("The person has taken you to what looks like a lab on the other side of the town.",3)
            pp("Suddenly realising you don't know the person name, you ask for the person's name.",3)
            pp("The person replies, I'm Jane Foster.",2)
            pp("Jane asks you your name.",3)
            pp("""
1. Thor, son of Odin.
2. Donald Blake.
""",1)
            choice6 = input("What do you tell her?:")
            if choice6 == "1":
                counter += 1
                pp("You have told Jane your real name and she suggests that you should take the name, Donald Blake.",5)
                pp("You accept the name and follow Jane into the lab.",3)
                pp("Here Jane shows you her work and explains to you what it means.",3)
                pp("While Jane goes to make a phone call, you are reading about voids and nebulas not taking in a word when two men storm through the door.",6)
                pp("Their sudden appearance startles you and you jump up ready for a fight.",3)
                pp("But the men just stand there and look at you.",3)
                pp("Then they advance and something hits you in the back of the head.",3)
                pp("You have been shot.",3)
                pp("You have died.",3)
                pp("You survived" ,counter, "choices.",1)
                again = input("Do you want to play again?:")
                if again == "yes":
                    po(2,menu.py)
                if again == "no":
                    time.sleep(3)
                    exit()
            if choice6 == "2":
                counter += 1
                pp("Jane says that she likes that name and that it was the name of her ex.",3)
                pp("Two people come out from what looks like the kitchen and they ask Jane what your name is.",4)
                pp("Jane tells them your name and that the two people are called Darcy Lewis and Erik Selvig.",5)
                pp("You tell the three people that you have to find Mjölnir.",2)
                pp("Jane, Darcy and Erik look at you like your mad.",2)
                pp("You explain about Mjölnir and about Asgard.",2)
                pp("Jane says that when you landed there was another explosion 3 miles away.",2)
                pp("You ask if you can go to the crash site and get Mjölnir.",2)
                pp("Jane agrees but before you leave she suggests you put on something more suited to Earth.",2)
                pp("After you have changed you set out in the car to the crash site.",2)
                pp("While on the way the crash site it starts to rain.",2)
                pp("You have arrived at the site and it is swarming with SHIELD agents.",3)
                pp("""
1. Storm in and mow down anyone in your path.
2. Stay where you are and strategize.
""",1)
                choice7 = input("What do you do?:")
                if choice7 == "2":
                    counter += 1
                    pp("You look around the area and how hard this is going to be hits you.",4)
                    pp("But thats not the only thing that hits you, something hard to the back of the head.",5)
                    pp("You have died. Nice try.",3)
                    pp("You survived" ,counter, "choices.",1)
                    again = input("Do you want to play again?:")
                    if again == "yes":
                        po(2,menu.py)
                    if again == "no":
                        exit()
                if choice7 == "1":
                    counter += 1
                    pp("You jump out the car and run full pelt smashing through the door.",3)
                    pp("You take down 1, 2, 3 guys while running down a corridor and see 6 more armed agents.",3)
                    pp("""
1. Run at them and hope for the best.
2. Turn around and try another route.
""",1)
                    choice9 = input("What do you do?")
                    if choice9 == "2":
                        counter += 1
                        pp("You turn around and run back up the corridor.",3)
                        pp("You round the corner and there is a sudden sound like a gun shot.",3)
                        pp("You have been shot. :(",3)
                        pp("You have died. Nice try.",3)
                        pp("You survived" ,counter, "choices.",1)
                        again = input("Do you want to play again?:")
                        if again == "yes":
                            po(2,menu.py)
                        if again == "no":
                            exit()
                    if choice9 == "1":
                        counter += 1
                        pp("You take down all six in a couple of seconds and race through the door.",3) 
                        pp("You see Mjölnir and go to take it.",2)
                        pp("You pull, nothing happens. You pull harder, nothing happens.",3)
                        pp("You know something is wrong.",3)
                        pp("Two people grab you under the arms and pull you away from your hammer.",3)
                        pp("They take you to a room where Jane is waiting.",3)
                        pp("Jane takes you back to the lab and you stay the night.",3)
                        pp("You wake up to an loud explosion.",2)
                        pp("""
1. Yes
2. No
""",1)
                        choice10 = input("Do you investigate? ")
                        if choice10 == "2":
                            counter += 1
                            pp("You decide that this noise is not worth your time and you fall asleep again.",5)
                            pp("You don't notice the sharp pain in the middle of your chest",4)
                            pp("The last thing you remember is a strong smell of coffee.",4)
                            pp("You have been stabed.",2)
                            pp("You have died. Nice try.",3)
                            pp("You survived" ,counter, "choices.",1)
                            again = input("Do you want to play again? ")
                            if again == "yes":
                                po(2,menu.py)
                            if again == "no":
                                exit()
                        if choice10 == "1":
                            counter += 1
                            pp("You burst through the hall door with your shirt on backwards and onto the street.",4)
                            pp("You turn and see the destroyer tearing up the coffee shop.",3)
                            pp("You pick up a metal rod and impale the destroyer through the back.",3)
                            pp("The destroyer turns around it's head grabs you and throws you across the road.",4)
                            pp("You grab a bin lid and chuck it at the destroyer.",3)
                            pp("The destroyer turns around and yells YOU ARE NOT WORTHY!!!!",3)
                            pp("You run at the destroyer and a pure energy beam hits you in the chest.",3)
                            pp("You get thrown back and go through the post office window.",3)
                            pp("You climb out of the wreckage and stop due to a whistling.",3)
                            pp("You turn around just in time to see Mjölnir flying towards.",3)
                            pp("You stretch out your hand, hope for the best and catch it.",3)
                            pp("The destroyer stops to look at you holding Mjölnir.",3)
                            pp("Your Asgardian armour flows over your skin and you hurl your hammer at the destroyer.",3)
                            pp("You call back Mjölnir and throw it back at the destroyer",3)
                            pp("The hammer goes through the destroyer's chest.",3)
                            pp("You strike the destroyer with lightning and it explodes.",3)
                            pp("You are congratulated for the work you have done and are allowed back into Asgard.",3)
                            pp("You tell Jane you have to leave but you will be back.",3)
                            pp("You open the Bifrost and return to Asgard.",3)
                            pp("You fly down the rainbow bridge and into the palace and see Loki on the throne.",3)
                            pp("""
1. Get angry with him.
2. Go get a coffee and then get angry with him.
""",1)
                            choice11 = ("What do you do? ")
                            if choice11 == "2":
                                counter += 1
                                pp("You quickly run to the coffee shop and then return.",4)
                                pp("You pull open the palace doors and the blade of Loki's sceptre is plunged into your chest.",5)
                                pp("You have died. Nice try.",3)
                                pp("You survived" ,counter, "choices.",1)
                                again = input("Do you want to play again? ")
                                if again == "yes":
                                    po(2,menu.py)
                                if again == "no":
                                    exit()
                                
                            if choice11 == "1":
                                counter += 1
                                pp("You grab him and hurl him through the palace doors.",3)
                                pp("You fly loki to the rainbow brigde and place him down with Mjölnir on his chest.",3)
                                pp("You shout at loki about you thought Odin was dead and Loki tells you that the frost giants are coming.",4)
                                pp("You think fast and decide to break the rainbow brigde to stop the giants.",3)
                                pp("Loki yells for you to stop but with one last strike your hammer goes through the brigde",3)
                                pp("You and Loki are pulled over the edge and you are holding loki from the infinite abyss.",3)
                                pp("You start to lift loki up to the edge but then suddenly... he lets go.",3)
                                pp("You have completed the game. Well done!!",3)
                                pp("You survived" ,counter, "choices.",1)
                                again = input("Do you want to play again? ")
                                if again == "yes":
                                    po(2,menu.py)
                                if again == "no":
                                    time.sleep(3)
                                    exit()
        if choice5 == "2":
            counter += 1
            pp("You enter the cafe and order a large coffee and drink it while eating your cookie.",2)
            pp("You have finished your coffee and cookie to your surprise the person that hit you with their car is still waiting outside looking expectant.",5)
            pp("Finally you give in and get in the car.",2)
            pp("The person takes you further into town.",3)
            pp("The person has taken you to what looks like a lab on the other side of the town.",3)
            pp("Suddenly realising you don't know the person name, you ask for the person's name.",3)
            pp("The person replies, I'm Jane Foster.",2)
            pp("Jane asks you your name.",1)
            pp("""
1. Thor, son of Odin.
2. Donald Blake.
""",1)
            choice8 = input("What do you tell her? ")
            if choice8 == "1":
                counter += 1
                pp("You have told Jane your real name and she suggests that you should take the name Donald Blake.",5)
                pp("You accept the name and follow jane into the lab.",3)
                pp("Here Jane shows you her work and explains to you what it means.",3)
                pp("While Jane goes to make a phone call, you are reading about voids and nebulas not taking in a word when two men storm through the door.",6)
                pp("Their sudden apperance startels you and you jump up ready for a fight.",3)
                pp("But the men just stand there and look at you.",3)
                pp("Then they advance and something hits you in the back of the head.",3)
                pp("You have been shot.",3)
                pp("You have died.",3)
                pp("You survived" ,counter, "choices.",1)
                again = input("Do you want to play again?:")
                if again == "yes":
                    po(2,menu.py)
                if again == "no":
                    time.sleep(3)
                    exit()
            if choice8 == "2":
                counter += 1
                pp("Here Jane shows you her work and explains to you what it means.",3)
                pp("While Jane goes to make a phone call, you are reading about voids and nebulas not taking in a word when two men storm through the door.",7)
                pp("Their sudden apperance startels you and you jump up ready for a fight.",3)
                pp("But the men just stand there and look at you.",3)
                pp("Then they advance and something hits you in the back of the head.",3)
                pp("You have been shot.",3)
                pp("You have died.",3)
                pp("You survived" ,counter, "choices.",1)
                again = input("Do you want to play again?:")
                if again == "yes":
                    po(2,menu.py)
                if again == "no":
                    time.sleep(3)
                    exit()
    if choice4 == "2":
        counter += 1
        pp("The town you have chosen is about 3 miles away, it will take you about 45 minutes.",3)
        pp("You reach the town and something doesn't feel right.",2)
        pp("It's very quiet and the town seemed deserted.",3)
        pp("Suddennly there is a loud crash, you whip around and there is a man standing with a gun...",4)
        pp("Without warning he pulls the trigger.",3)
        pp("There was nothing you could have done. You are dead.",3)
        pp("You survived" ,counter, "choices.",1)
        again = input("Do you want to play again????:")
        if again == "yes":
            po(2,menu.py)
        if again == "no":
            time.sleep(3)
            exit() 
