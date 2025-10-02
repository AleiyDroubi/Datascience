
def main():
    get_name()
    print (name)
   
def get_name():
    global name
    name=input("enter name: ") 
    age=input("enter your age: ")
    print("your name is",name)
    print("your age is",age)
    
main()



