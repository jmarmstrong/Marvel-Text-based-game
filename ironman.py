#ironman game file.
import time
import os
print("Hello, You have chosen to play as Ironman this particular time.")
time.sleep(2)
print("You walk into your lab and log on to your computer (top of the range)")
time.sleep(2)
print("You see that you have emails but you are tired.")
time.sleep(2)
print("""
1. Look at them.
2. Go to bed.
3. Get a coffee.
""")
choice = input("What do you do? ")
if choice == "1":
    print("hi")
