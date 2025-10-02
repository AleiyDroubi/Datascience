import time
import random
min=1
max=6
restart="y"
while restart=="y" or restart=="Y":
    print("Rolling the dice...")
    print("Their values are")
    time.sleep(2)
    print("Dice 1 \t Dice 2")
    print('~~~~~~~~~~~~~~~~~~')
    print(random.randint(min,max),"\t",(random.randint(min,max)))
    time.sleep(2)
    restart=input("Enter y to roll again: ")