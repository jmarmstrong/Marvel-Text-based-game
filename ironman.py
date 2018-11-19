#Ironman.py game file
import time
import os
def pp (text,pause):
    print(text)
    time.sleep(pause)
def po (pause,openfile):
    time.sleep(pause)
    os.startfile(openfile)
counter = 0
pp("Hello brave player, you have chosen to play as Ironman this particular time.",1)
pp("You walk into your lab and log on to your computer (top of the range).",1)
pp("You see that you have emails but you are very tired.",1)
pp("""
1. Look at the emails.
2. Go to bed.
3. Get a coffee.
""",1)
choice = input("What do you do? ")
if choice == "1":
    counter += 1
    pp("You open your emails and you see an email from an unknown person.",1)
    pp("You open the email and it says you are already dead.",1)
    pp("It explodes!!!",1)
    pp("You die. :(",1)
    pp("Please try again.",1)
    pp("You survived "+str(counter)+" choices.",1)
    again = input("Do you want to play again? ")
    if again == "yes":
        po(1,"menu.py")
    if again == "no":
        time.sleep(1)
        exit()
if choice == "2":
    counter += 1
    pp("You shut down your computer and go to your bedroom.",1)
    pp("You get into bed and quickly fall asleep.",1)
    pp("You dream that you are in a miltary vehicle going along a desert road.",1)
    pp("Suddenly an explosion shakes the car.",1)
    pp("You are told to stay in the car while the troops you are with jump out to counter attack.",1)
    pp("As the troops leave you sit waiting, then BANG!!",1)
    pp("You are thrown out of the car and you hit the floor with a crash.",1)
    pp("You crawl behind a rock and a few seconds later a missile hits the ground 4 feet from you.",1)
    pp("It says Stark Industries on it.",1)
    pp("""
1. Stay where you are.
2. Try and run.
3. Try to diffuse the missile.
""",1)
    choice2 = input("What do you do? ")
    if choice2 == "1":
        counter += 1
        pp("You lay back against a rock and close your eyes.",1)
        pp("3, 2, 1.",3)
        pp("BOOM!",1)
        pp("You die. :(",1)
        pp("Please try again.",1)
        pp("You survived "+str(counter)+" choices.",)
        again = input("Do you want to play again? ")
        if again == "yes":
            po(1,"menu.py")
        if again == "no":
            time.sleep(1)
            exit()
    if choice2 == "2":
        counter += 1
        pp("You scramble to your feet and take one step...",1)
        pp("BOOM!!!!!!!",1)
        pp("You wake up lying on a bed in what looks like a cave.",1)
        pp("You trying to sit up but you feel and pulling from your chest.",1)
        pp("You look down and see wires coming out from under your top.",1)
        pp("You look around and see a man sitting in a chair.",1)
        pp("The man says he is called Ho Yinsen and that you are in a cave in afganistan.",1)
        pp("He says that they will be coming soon because there is something they want you to do.",1)
        pp("A couple of minutes later 5 men turn up at the enterance of the room.",1)
        pp("They say that they want you to build a jericho missile.",1)
        pp("""
1. Agree
2. Refuse
""",1)
        choice4 = input("Choose wisely: ")
        if choice4 == "1":
            counter += 1
            #complete
        if choice4 == "2":
            counter += 1
            pp("They grab you and shove your head into a water bucket. Seems pointless really.",1)
            pp("They pull you out and put a bag over your head. Again pointless.",1)
            pp("They walk you out of the cave and take the bag off.",1)
            pp("You are dazzeled by the sunlight and you see piles of machinery.",1)
            #complete
    if choice2 == "3":
        counter += 1
        pp("You crawl towards the missile and you open the side of the missile.",1)
        pp("You see a green, black and red wire.",1)
        pp("""
1. Green
2. Black
3. Red.
""",1)
        choice3 = input("Which do you cut? ")
        if choice3 == "1":
            counter += 1
            pp("You cut the green wire and YOU explode.",1)
            pp("Not the missile.",1)
            pp("You die. :(",1)
            pp("Please try again.",1)
            pp("You survived "+str(counter)+" choices.",1)
            again = input("Do you want to play again? ")
            if again == "yes":
                po(1,"menu.py")
            if again == "no":
                time.sleep(1)
                exit()
        if choice3 == "2":
            counter += 1
            pp("You cut the black wire and you turn around...",1)
            pp("You die. :(",1)
            pp("You had coffee that morning.",1)
            pp("Please try again.",1)
            pp("You survived "+str(counter)+" choices.",1)
            again = input("Do you want to play again? ")
            if again == "yes":
                po(2,"menu.py")
            if again == "no":
                time.sleep(1)
                exit()
        if choice3 == "3":
            counter += 1
            pp("You cut the red wire and...",1)
            pp("You get hit in the face with another missile.",1)
            pp("You die. :(",1)
            pp("Please try again.",1)
            pp("You survived "+str(counter)+" choices.",1)
            again = input("Do you want to play again? ",1)
            if again == "yes":
                po(1,"menu.py")
            if again == "no":
                time.sleep(2)
                exit()
if choice == "3":
    counter += 1
    pp("You get up from your chair and leave the room.",1)
    pp("You walk into the hall and turn on the coffee machine.",1)
    pp("""
1. Decaf.
2. Non Decaf.
""",1)
    choicecoffee = input("")
    pp("You grab a mug and turn back to the coffee machine.",1)
    pp("You die. :(",1)
    pp("You were hit in the face with boiling hot coffee.",1)
    pp("The last through you know is the smell of strong coffee.",1)
    pp("Please try again.",1)
    pp("You survived "+str(counter)+" choices.",1)
    again = input("Do you want to play again? ")
    if again == "yes":
        po(1,"menu.py")
    if again == "no":
        time.sleep(2)
        exit()
