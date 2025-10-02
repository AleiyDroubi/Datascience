import time
import random
ans='Y'
print("This program plays 'Rock','Paper','Siscors'. ")
time.sleep(1.7)
while ans=="Y" or ans=="y":
    player = (input('Enter your choice (r,p,s): '))
    computer = random.choice(['r', 'p', 's'])
    if player.lower() == computer:
        print("It's a tie!")
    elif (player.lower()=='r' and computer=='s') or (player.lower()=='s' and computer=='p')\
          or (player.lower()=="p" and computer=="r"):
        time.sleep(1)
        print("You win!")
    else:
        time.sleep(1)
        print("You lose!")
    time.sleep(1)    
    ans=input("Enter 'y' to play again. ")
    time.sleep(2)
print("Thanks for playing.")
