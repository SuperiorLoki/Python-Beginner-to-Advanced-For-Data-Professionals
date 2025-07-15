'''
Python has built-in exceptions that means when the code does not run properly
When an exception(error) occurs at a certain line, the rest of the code will not run so we need to use exception handling
'''

x = int(input("Enter Number 1: "))
y = int(input("Enter number 2: "))
d=0
try:
    d = x/y
    a = "lebron" + 23
#Good to always specify the type of exception but you dont HAVE to per se. The variable "ze" will store the exception
except ZeroDivisionError as ze:
    print("The 2nd number cannot be 0 as you cannot divide a number by 0")
    print(f"The exception that occured was: {ze}")
#You can also have multiple excepts
except TypeError as te:
    print("You cannot add a number to a string")
    print(f"The exception that occured was: {te}")
#Or just any exception in general. This will tell us the type of exception but it is not encouraged
except Exception as e:
    print(f"Exception type: ")
#If there is an error or not, finally will run
finally:
    print("This code needs to be run.")


print("Number 1/Number 2: ", d)