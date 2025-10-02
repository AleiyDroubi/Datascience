choice=["Rock", "Paper", "Scissers"]
Cpu=0
User=0
def game():
    if(user==cpu):
        print(user,cpu, "Draw")
    elif(user=='Paper' and cpu=='Rock'):
        print(user,cpu,"User wins")
        global User
        User += 1
    elif(user=='Rock' and cpu=='Scissors'):
        print(user,cpu, "User wins")
        User += 1
    elif(user=='Scissors' and cpu=='Paper'):
        print(user,cpu, "User wins")
        User += 1
    else:
        print(user, cpu ,"Cpu wins :)")
        global Cpu
        Cpu += 1
    
import random
cpu=random.choice(choice)
user=input("Enter 'Rock','Paper','Scissors': ")
for x in range(5):
    game()
    cpu=random.choice(choice)
    user=input("Enter 'Rock','Paper','Scissors': ")
game()    
print("Final score is: ",User,"     ",Cpu)
