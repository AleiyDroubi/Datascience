import random
def main():
    even=0
    odd=0
    for i in range(1,101):
        num= random.randint(1,1000)
        if(num%2==0):
            even+=1
        else:
            odd+=1

    print("Total even numers=",even)
    print("Total odd numbers=",odd)
main()


