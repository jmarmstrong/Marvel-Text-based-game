#wwmdf start menu.
import time
import os
print("Hello and welcome to the decide your own destiny marvel edition.")
time.sleep(2)
print("""
1. Start.
2. Settings.
3. Credits.
4. Exit.
""")
choice1 = input("Prepare your self and enter your choice: ")
if choice1 == "4":
    exit()
if choice1 == "3":
    print("CREDITS")
    time.sleep(2)
    print("Main designer, marvel specialist, owner and maker of Thor, Loki, Captin America, Red Skull : Oliver Cole.")
    time.sleep(3)
    print("Code specialist and maker of Iron man and Ultron: Joseph Armstrong")
    time.sleep(2)
    print("Main code : Python")
    time.sleep(2)
    print("Code version: 3.4.3")
    time.sleep(2)
    print("A special thanks to Marvel Studios, Stan Lee, Jack Kirby and Steve Ditko.")
    time.sleep(4)
    exit()
if choice1 == "2":
    print("JK there are no settings")
    time.sleep(1)
    exit()
if choice1  == "1":
    time.sleep(2)
    print("Hello brave player, you have selected to play this game at your own risk. First chose your side.")
    time.sleep(2)
    print("""
1. Good
2. Evil
""")
    choice2 = input("Please enter your side (Beware after this point there is no going back.) : ")
if choice2 == "1":
    time.sleep(1)
    print("Welcome to the good side in this battle. You have chosen to fight the evil and make the good choices. Well done.")
    print("""
1. Tony Stark (Iron Man)
2. Donald Blake (Thor)
3. Steve Rogers (Captain America)
""")
    choicehero = input("Please choose your hero: ")
    if choicehero == "1":
        os.startfile("ironman.py")
    if choicehero == "2":
        os.startfile("thor.py")
    if choicehero == "3":
        os.startfile("cap.py")
if choice2 == "2":
    time.sleep(1)
    print("You have made the right choice. The all consuming and all powerful darkness has chosen you to assist us to an ultimate victory. On this route you will find you have power and abilities you dreamed of as a child. Once again you have made the right choice")
    print("""
1. Ultron
2. Loki
3. Johann Schmidt (Red Skull)
""")
    choicevillan = input("Please choose you villan: ")
    if choicevillan == "1":
        os.startfile("ultron.py")
    if choicevillan == "2":
        os.startfile("loki.py")
    if choicevillan == "3":
        os.startfile("rs.py")
        
        
    
