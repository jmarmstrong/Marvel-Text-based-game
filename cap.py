#Cap.py game file
import time
import os
def pp (text,pause):
    print(text)
    time.sleep(pause)
def po (pause,openfile):
    time.sleep(pause)
    os.startfile(openfile)
pp("You walk out of the theatre and feel like there is nothing to do, and you start walking down the road.",3)
pp("As you start walking down the road you see someone getting mugged and beaten up. you know what to do! Do you... ",3)
pp("""
1. run over and help?
2. finish the rest of the popcorn and enjoy the show?
3. go and get a coffee?
""",3)
choice = input("What do you do? ")
if choice == "3":
    pp("You think that you should help, but you really like coffee so you leave.",3)
    pp("You make your way through the hood until you reach a crossroad.",3)
    pp("The person that you probably should have helped is probably dead by now due to the fact that you where the only one there to stop it but maybe you can still help them",5)
    pp("""
1. GO back and help the person.
2. go left.
3. go right.
4. continue to go forwards.
""",3)
    choice1 = input("What to do")
    if choice1 == "1":
        pp("You sprint down the road back to the theatre but you are to late",3)
        pp("#FAIL",2)
        again = input("Do you want to play again? ")
        if again == "yes":
            time.sleep(2)
            os.startfile("menub.py")
        if again == "no":
            time.sleep(3)
            exit()
    if choice1 == "2":
        print("You turn left and you see some Nazi zombie ...")
        time.sleep(10)
        print("Then a car come out of nowhere with spikes covering it and runs all of them over")
        time.sleep(3)
        print("You stand there for about 20 seconds")
        time.sleep(20)
        print("Then you contiune down the road and protend that it never happend. As you contiune down the road you finlly find the coffee shop. But....")
        time.sleep(4)
        print("There is a sign on the door do you.")
        print("""
        1.Read the sign
        2.Try the door.
        """)
        door = input("Want do you do")
        if door == "1":
            print("You read the sign that says it is closed until 2000")
            time.sleep(3)
            print("You say to yourself it would be better to be frozen in ice until then.")
            time.sleep(5)
            print("It is a hollow victory for you. But I guess you win then?")
            time.sleep(3)
            print("Well done you win because you didn't die, but you didn't play the game properly so wait here for 10minuets and 30seconds to make up for you not play the whole story.")
            time.sleep(30)
            print("you got trolled you troll.")
            time.sleep(600)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
            if again == "no":
                time.sleep(3)
                exit()
        if door == "2":
            print("You try the handle but it is lock so you red the sign it says it is closed until 2000")
            time.sleep(3)
            print("You say to yourself it would be better to be frozen in ice until then.")
            time.sleep(5)
            print("It is a hollow victory for you. But I guess you win then?")
            time.sleep(3)
            print("Well done you win because you didn't die, but you didn't play the game properly so wait here for 10minuets and 30seconds to make up for you not play the whole story.")
            time.sleep(30)
            print("you got trolled you troll.")
            time.sleep(600)
            again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
            if again == "no":
                time.sleep(3)
                exit()
    if choice1 == "3":
        print("You go right because right is always right")
        time.sleep(2)
        print("You walk down the steet and it look like there was a zombie apocalips there.")
        time.sleep(3)
        print("You say to yourself that it is quiet... too quiet...")
        time.sleep(10)
        print("Suddenly the the wall all broke down and there were zombies every where of some reason.")
        time.sleep(3)
        print("you start to run but they are slow catching up to you then you see the road divid there are to way to go left and right. What do you do?")
        time.sleep(4)
        print(" ")
        print("1. Go left")
        print("2. Go right")
        print("3. Stay and fight")
        print(" ")
        time.sleep(20)
        print("But befor you can reacted a nuke hit you in the face.")
        print("you died.")
        time.sleep(3)
        print("And so is everyone else!")
        again = input("Do you want to play again? ")
        if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
            if again == "no":
                time.sleep(3)
                exit()
    if choice1 == "4":
        print("You contiue going straight ahead.")
        time.sleep(2)
        print("You think of all the adventers that you could have gone on if you help that guy.")
        time.sleep(2)
        print("You think of your friends and you think of the girl of your dream being there.")
        time.sleep(4)
        print("As the sun start to set you know that it would look cool if you became a hero and did this if you had become...")
        time.sleep(2)
        print("Captain America the first Avenger!")
        time.sleep(3)
        print("Role credits!")
        again = input("Do you want to play again? ")
            if again == "yes":
                time.sleep(2)
                os.startfile("menub.py")
            if again == "no":
                time.sleep(3)
                exit()
if choice == "2":
    print("You just stand there and grab some  more popcorn and wait for it to end. ")
    time.sleep(4)
    print("Out of the corner of his eyes he sees you standing there. You know what you've got your self into, As the look he gives you....")
    time.sleep(6)
    print("With a burning rage he punch your face and then kick you where it hurts. ")
    print("He continues to beat you up and finally throw you over to the bins. Out of the corner of your eyes you see a bin lid. What do you do...")
    print("""
    1.pick up the bin lid
    2.try and swing at him
    """)
if choice == "1":
    print("You run towards the guy and shout stop.")
    time.sleep(2)
    print("He turns around a gives you the LOOK....")
    time.sleep(6)
    print("With a burning rage he punch your face and then kick you where it hurts. ")
    print("He continues to beat you up and finally throw you over to the bins. Out of the corner of your eyes you see a bin lid. What do you do...")
    time.sleep(2)
    choice1 = input("you know what to do")
