"""Tip, the waiter
Outline:
Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant.
 Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total 
 amount you should pay."""

def calculate(bill,percent):
    total=bill*(1+0.01*percent)
    total=round(total,2)
    print(f"Please pay ${total}")
calculate(150,20)



"""Cube of the cube
Outline:
Define a function to find a cube and define another
 function which let execute the cube function
 if the number is divisible by 3"""

def cube(number):
    return number*number*number
def three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
print(three(15))
print(three(12))



"""Factorial
Outline:
Write a program to find the factorial using recursive 
function"""

def factorial(x):
    '''This is a recursive function to find the factorial of an integer'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print(factorial (0))
print(factorial (1))
print(factorial (2))
print(factorial (3))
print(factorial (4))
print(factorial (5))
print(factorial (6))
print(factorial (7))
print(factorial (8))
print(factorial (9))
print(factorial (10))