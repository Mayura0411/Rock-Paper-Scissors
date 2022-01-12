from random import randint
import time
play=["rock","paper","scissors"]
computer=play[randint(0,2)]
player=False
while player==False:
    player=input("rock,paper,scissors")
    if player==computer:
        print("Tie!")
    elif player=="rock":
        if computer=="paper":
            print("computer chosses",computer)
            time.sleep(2)
            print("You loose :(")
        else:
            print("computer chosses",computer)
            time.sleep(2)
            print("you win :)")
    elif player=="paper":
        if computer=="scissors":
            print("computer chosses",computer)
            time.sleep(2)
            print("You loose :(")
        else:
            print("computer chosses",computer)
            time.sleep(2)
            print("you win :)")
    elif player=="scissors":
        if computer=="rock":
            print("computer chosses",computer)
            time.sleep(2)
            print("You loose :(")
        else:
            print("computer chosses",computer)
            time.sleep(2)
            print("you win :)")
    else :
        print("check your spelling")
    player=False
    computer=play[randint(0,2)]

