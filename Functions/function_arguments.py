'''
#Putting a star in front of args will allow us to have an unlimited amount of parameters when calling
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


total = sum_all(1,2,3,4,5)
'''

#You can use kwargs for keywords in parameters like here
#You treat kwargs like a dictionary
def company_info(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])

company_info(ticker='AAPL', ceo="Tim Cook", revenue="200 billion")


def find_square(a):
    return a*a

#One line way of defining a function (you are squaring the parameter a here)
x = lambda a: a*a

y = lambda a,b: a+b



