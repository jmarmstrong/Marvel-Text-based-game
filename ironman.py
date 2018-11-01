#Ironman.py gamefile
import time
import os
counter = 0
print("Hello brave player, you have chosen to play as Ironman this particular time.")
time.sleep(2)
print("You walk into your lab and log on to your computer (top of the range).")
time.sleep(2)
print("You see that you have emails but you are very tired.")
time.sleep(2)
print("""
1. Look at the emails.
2. Go to bed.
3. Get a coffee.
""")
choice = input("What do you do? ")
if choice == "1":
    counter += 1
    print("You open your emails and you see an email from an unknown person.")
    time.sleep(1)
    print("You open the email and it says you are already dead.")
    time.sleep(1.5)
    print("It explodes!!!")
    time.sleep(1)
    print("You die. :(")
    time.sleep(1)
    print("Please try again.")
    time.sleep(1)
    print("You survived" ,counter, "choices.")
    time.sleep(1)
    again = input("Do you want to play again? ")
    if again == "yes":
        time.sleep(2)
        os.startfile("menu.py")
    if again == "no":
        time.sleep(2)
        exit()
if choice == "2":
    counter += 1
    print("You shut down your computer and go to your bedroom.")
    time.sleep(1)
    print("You get into bed and quickly fall asleep.")
    time.sleep(1)
    print("You dream that you are in a miltary vehicle going along a desert road.")
    time.sleep(1)
    print("Suddenly an explosion shakes the car.")
    time.sleep(1)
    print("You are told to stay in the car while the troops you are with jump out to counter attack.")
    time.sleep(1)
    print("As the troops leave you sit waiting, then BANG!!")
    time.sleep(1)
    print("You are thrown out of the car and you hit the floor with a crash.")
    time.sleep(1)
    print("You crawl behind a rock and a few seconds later a missle hits the ground 4 feet form you.")
    time.sleep(1)
    print("It says Stark Industries on it.")
    time.sleep(1)
    print("""
1. Stay where you are.
2. Try and run.
3. Try to diffuse the missle.
""")
    choice2 = input("What do you do? ")
    if choice2 == "1":
        counter += 1
        print("You lay back against a rock and close your eyes.")
        time.sleep(1)
        print("3, 2, 1.")
        time.sleep(1)
        print("BOOM!")
        time.sleep(1)
        print("You die. :(")
        time.sleep(1)
        print("Please try again.")
        time.sleep(1)
        print("You survived" ,counter, "choices.")
        time.sleep(1)
        again = input("Do you want to play again? ")
        if again == "yes":
            time.sleep(2)
            os.startfile("menu.py")
        if again == "no":
            time.sleep(2)
            exit()
    if choice2 == "2":
        counter += 1
        print("You scramble to your feet and take one step...")
        time.sleep(1)
        print("BOOM!!!!!!!")
        time.sleep(1)
        print("You wake up lying on a bed in what looks like a cave.")
        time.sleep(2)
        print("You trying to sit up but you feel and pulling from you chest.")
        time.sleep(2)
        print("You look down and see wires coming out from under you top.")
    if choice2 == "3":
        counter += 1
        print("You crawl towards the missile and you open the side of the missile.")
        time.sleep(2)
        print("You see a green, black and red wire")
        time.sleep(2)
        print("""
1. Green
2. Black
3. Red.
""")
        choice3 = input("Which do you cut? ")
        if choice3 == "1":
            counter += 1
            print("You cut the green wire and YOU explode.")
            time.sleep(1)
            print("Not the missle.")
            time.sleep(1)
            print("You die. :(")
            time.sleep(1)
            print("Please try again.")
            time.sleep(1)
            print("You survived" ,counter, "choices.")
            time.sleep(1)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menu.py")
            if again == "no":
                time.sleep(2)
                exit()
        if choice3 == "2":
            counter += 1
            print("You cut the black wire and you turn around...")
            time.sleep(1)
            print("You die. :(")
            time.sleep(1)
            print("You had coffee that morning.")
            time.sleep(1)
            print("Please try again.")
            time.sleep(1)
            print("You survived" ,counter, "choices.")
            time.sleep(1)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menu.py")
            if again == "no":
                time.sleep(2)
                exit()
        if choice3 == "3":
            counter += 1
            print("You cut the red wire and...")
            time.sleep(1)
            print("You get hit in the face with another missile.")
            time.sleep(1)
            print("You die. :(")
            time.sleep(1)
            print("Please try again.")
            time.sleep(1)
            print("You survived" ,counter, "choices.")
            time.sleep(1)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menu.py")
            if again == "no":
                time.sleep(2)
                exit()
if choice == "3":
    counter += 1
    print("You get up from your chair and leave the room.")
    time.sleep(1)
    print("You walk into the hall and turn on the coffee machine.")
    time.sleep(2)
    print("You grab a mug and turn back to the coffee machine.")
    time.sleep(1)
    print("You die. :(")
    time.sleep(2)
    print("You were hit in the face with boiling hot coffee.")
    time.sleep(1)
    print("The last through you know is the smell of strong coffee.")
    time.sleep(1)
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
