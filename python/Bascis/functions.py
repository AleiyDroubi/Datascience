def my_function():
  print("Hello from a function") 
my_function() #calls the function
def my_function_with_args(fname, lname):
  print(fname + " " + lname)

my_function_with_args("John", "Doe") #calls the function with arguments

#unknown number of arguments
def my_function_unknown_args(*kids):
  print("The youngest child is " + kids[2])
my_function_unknown_args("Emil", "Tobias", "Linus") #calls the function with unknown number of arguments

#return value
def my_function_return(x):
  return 5 * x
print(my_function_return(3)) #prints 15
print(my_function_return(5)) #prints 25
print(my_function_return(9)) #prints 45

#recursive function
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
tri_recursion(6) #prints 1, 3, 6, 10, 15, 21