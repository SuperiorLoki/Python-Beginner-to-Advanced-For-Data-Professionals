#Make sure that you make the input an int with int() because an input is automatically a string
num = int(input("Enter a number: "))

'''
if num % 2 ==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")
'''
#OR

message = "Number is even" if num % 2 ==0 else "Number is odd"
print(message)

#OR
'''
if not num % 2 == 0:
    print("Odd number")
'''

if num >8 and num % 2 ==0:
    print(f"{num} is both greater than 8 and is an even number")
else:
    print(f"{num} is less than 8 and it is odd")

#You can also replace the and with an 'or' operator