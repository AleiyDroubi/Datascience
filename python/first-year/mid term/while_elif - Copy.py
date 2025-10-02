
def main():
     ans="Y"
     while ans =="y" or ans=="Y":
          seconds=float(input("Enter number of seconds from 60:infinit "))
          while seconds<=0:
               print("WRONG INPUT \nTRY AGAIN: ")
               seconds=float(input("Enter number of seconds from 60:infinit ")) 
         
          if seconds>=60 and seconds<3600:
               min=seconds/60 
               print("your number in seconds =",round(min,2),"minutes")
          elif seconds<60 and seconds>0:
               print(seconds,"seconds")
          elif seconds>=3600 and seconds <86400:
               days=seconds/3600
               print("your number in days =",round(days,2),"days")
          elif seconds>=86400:
               years=seconds/86400
               print("your seconds in years =",round(years,2),"years")  
          ans=input("Enter 'Y' to repeat the process and to stop enter any other element: ")
main()
