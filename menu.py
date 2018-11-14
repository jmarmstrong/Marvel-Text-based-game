#wwmdf start menu.
import time
import os
def ps (text,sleep):
    print(text)
    time.sleep(sleep)
ps("Hello and welcome to the decide your own destiny marvel edition.",2)
ps("""
1. Start.
2. Settings.
3. Credits.
4. Exit.
""",1)
choice1 = input("Prepare your self and enter your choice: ")
if choice1 == "4":
    exit()
if choice1 == "3":
    ps("CREDITS",2)
    ps("Main designer, CEO, marvel specialist, maker of Thor and Ironman : Oliver Cole.",2)
    ps("Code specialist and maker of Menu and Menub: Joseph Armstrong",2)
    ps("Comedy specialist and maker of Captin America: Emmamuel Andal.",2)
    ps("Main code : Python",2)
    ps("Code version: 3.4.3",2)
    ps("A special thanks to Marvel Studios, Stan Lee, Jack Kirby and Steve Ditko For Inspiration.",5)
    exit()
if choice1 == "2":
    ps("Joking there are no settings",1)
    exit()
if choice1  == "1":
    time.sleep(2)
    ps("Hello brave player, you have selected to play this game at your own risk. First chose your side.",2)
    ps("""
1. Good
2. Evil
""",1)
    choice2 = input("Please enter your side (Beware after this point there is no going back.) : ")
if choice2 == "1":
    time.sleep(1)
    ps("Welcome to the good side in this battle. You have chosen to fight the evil and make the good choices. Well done.",1)
    ps("""
1. Tony Stark (Iron Man)
2. Donald Blake (Thor)
3. Steve Rogers (Captain America)
""",1)
    choicehero = input("Please choose your hero: ")
    if choicehero == "1":
        os.startfile("ironman.py")
    if choicehero == "2":
        os.startfile("thor.py")
    if choicehero == "3":
        os.startfile("cap.py")
if choice2 == "2":
    time.sleep(1)
    ps("You have made the right choice. The all consuming and all powerful darkness has chosen you to assist us to an ultimate victory. On this route you will find you have power and abilities you dreamed of as a child. Once again you have made the right choice",1)
    ps("""
1. Doctor DOOM
2. Magneto
3. The green goblin
""",1)
    choicevillan = input("Please choose you villan: ")
    if choicevillan == "1":
        os.startfile("doom.py")
    if choicevillan == "2":
        os.startfile("mag.py")
    if choicevillan == "3":
        os.startfile("tgg.py")
