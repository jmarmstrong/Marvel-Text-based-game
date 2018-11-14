import time
import os
def ps (text,time):
    print(text)
    time.sleep(time)
ps("Hello and wellcome to the decide your own destiny marvel edition.",1)
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
    ps("Main designer and CEO: Oliver Cole.",2)
    ps("Code specialist: Joseph Armstrong",2)
    ps("Comedy specialist: Emmamuel Andal.",2)
    ps("Main code : Python",2)
    ps("Code version: 3.4.3",2)
    ps("A special thanks to Marvel Studios, Stan Lee, Jack Kirby and Steve Ditko for inspiration.",6)
    exit()
if choice1 == "2":
    ps("Joking theres no settings.",1)
    exit()
if choice1 == "1":
    time.sleep(2)
    ps("Hello brave player, you have selected to play this game at your own risk. First chose your side.",2)
    ps("""
1. Good
2. Evil
""",1)
choice2 = input("Please enter your side (Beware after this point there is no going back): ")
if choice2 == "1":
    ps("Welcome to the good side in this battle. You have chosen to fight the evil and make the good choices. Well done.",1)
    ps("""
1. Tony Stark (Iron Man)
2. Donald Blake (Thor)
3. Steve Rogers (Captain America)
Bonus
4. The MCU (good guys).
""",1)
    choicehero = input("Please choose your hero: ")
    if choicehero == "1":
        os.startfile("ironman.py")
    if choicehero == "2":
        os.startfile("thor")
    if choicehero == "3":
        os.startfile("cap.py")
    if choicehero == "4":
        os.startfile("MCU.py")
if choice2 == "2":
    ps("You have made the right choice. The all consuming and all powerful darkness has chosen you to assist us to an ultimate victory. On this route you will find you have power and abilities you dreamed of as a child. Once again you have made the right choice.,1")
    ps("""
1. Ultron
2. loki
3. Johann Schmidt (Red Skull)
Bonus
4. Thanos
""",1)
    choicevillan = input("please chose your villan: ")
    if choicevillan == "1":
        os.startfile("ultron.py")
    if choicevillan == "2":
        os.startfile("loki.py")
    if choicevillan == "3":
        os.startfile("rs.py")
    if choicevillan == "4":
        os.startfile("The_Mad_Titan.py")
    
