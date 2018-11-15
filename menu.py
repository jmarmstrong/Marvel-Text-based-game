#elemental industries menu.py
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
    ps("Comedy specialist and maker of Captian America: Emmamuel Andal.",2)
    ps("Main code : Python",2)
    ps("Code version: 3.4.3",2)
    ps("""
A special thanks to Marvel Studios.
Stan Lee (28 December 1922 - 12 November 2018),
Jack Kirby (28 August 1917 - 6 February 1994),
Steve Ditko (2 November 1927 - June 2018) For Inspiration.
They will forever be remembered.
All of this is for you.
The men that showed that imagination really can change the world.
Excelsior!!
Now and forever more.
""",30)
    exit()
if choice1 == "2":
    ps("Joking there are no settings",1)
    ps("""
1. Start.
2. Settings.
3. Credits.
4. Exit.
""",1)
choice3 = input("Prepare your self and enter your choice: ")
if choice3 == "4":
    exit()
if choice3 == "3":
    ps("CREDITS",2)
    ps("Main designer, CEO, marvel specialist, maker of Thor and Ironman : Oliver Cole.",2)
    ps("Code specialist and maker of Menu and Menub: Joseph Armstrong",2)
    ps("Comedy specialist and maker of Captian America: Emmamuel Andal.",2)
    ps("Main code : Python",2)
    ps("Code version: 3.4.3",2)
    ps("""
A special thanks to Marvel Studios.
Stan Lee (28 December 1922 - 12 November 2018),
Jack Kirby (28 August 1917 - 6 February 1994),
Steve Ditko (2 November 1927 - June 2018) For Inspiration.
They will forever be remembered.
All of this is for you.
The men that showed that imagination really can change the world.
Excelsior!!
Now and forever more.
""",30)
    exit()
if choice3 == "2":
    ps("Joking there are no settings",1)
    exit()
if choice3  == "1":
    time.sleep(2)
    ps("Hello brave player, you have selected to play this game at your own risk. First chose your side.",2)
    ps("""
1. Good
2. Evil
""",1)
    choice4 = input("Please enter your side (Beware after this point there is no going back.) : ")
if choice4 == "1":
    time.sleep(1)
    ps("Welcome to the good side in this battle. You have chosen to fight the evil and make the good choices. Well done.",1)
    ps("""
1. Tony Stark (Iron Man)
2. Donald Blake (Thor)
3. Steve Rogers (Captain America)
""",1)
    choicehero2 = input("Please choose your hero: ")
    if choicehero2 == "1":
        os.startfile("ironman.py")
        exit()
    if choicehero2 == "2":
        os.startfile("thor.py")
        exit()
    if choicehero2 == "3":
        os.startfile("cap.py")
        exit()
if choice4 == "2":
    time.sleep(1)
    ps("You have made the right choice. The all consuming and all powerful darkness has chosen you to assist us to an ultimate victory. On this route you will find you have power and abilities you dreamed of as a child. Once again you have made the right choice",1)
    ps("""
1. Doctor DOOM
2. Magneto
3. The green goblin
""",1)
    choicevillan2 = input("Please choose you villan: ")
    if choicevillan2 == "1":
        os.startfile("doom.py")
        exit()
    if choicevillan2 == "2":
        os.startfile("mag.py")
        exit()
    if choicevillan2 == "3":
        os.startfile("tgg.py")
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
        exit()
    if choicehero == "2":
        os.startfile("thor.py")
        exit()
    if choicehero == "3":
        os.startfile("cap.py")
        exit()
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
        exit()
    if choicevillan == "2":
        os.startfile("mag.py")
        exit()
    if choicevillan == "3":
        os.startfile("tgg.py")
        exit()
