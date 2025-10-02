import random
def main():
    min=1
    max=20
    answer="y"

    while(answer=="y"or answer== "Y"):
        randome_number=random.randint(min,max)
        num=int(input("Enter a number: "))
        
        while(True):
            if(num==randome_number):
                print("Correct")
                break
            elif(num>randome_number):
                print("Too high")
            elif(num<randome_number):
                print("Too low")    
            num=int(input("Enter a number "))
        print(randome_number)
        answer=input("Enter Yes/y to try again else enter no/n ")
main()        