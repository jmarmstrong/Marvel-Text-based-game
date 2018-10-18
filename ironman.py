#ironman game file
import time
import os
counter = 0
print("Hello, You have chosen to play as Ironman this particular time.")
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
    print("You open your emails and you see an email from and unknown person.")
    time.sleep(1)
    print("You open the email and it says you are already dead.")
    time.sleep(1.5)
    print("It explodes!!!")
    time.sleep(1)
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
if choice == "2":
    counter += 1
    print("hi ethan.")
if choice == "3":
    counter += 1
    print("hi")
