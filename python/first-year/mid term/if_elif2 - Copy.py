A=90
B=75
C=60
D=50
def main():    
   score=float(input("Enter your score from 0:100 "))
   get_score(score)

def get_score(score):
   if score>=A:
      print("your grade is A ")
   elif score>=B:
      print("your grade is B ")
   elif score>=C:
      print("your score is C ")
   elif score>=D:
      print("your score is D ") 
   else:
      print("you have failed")

main()
