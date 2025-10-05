"""Sum of Natural Numbers
Outline:
Write a program to find the sum of natural numbers."""

n=int(input("Please enter the number you want to add:"))
sum=0
i=1
while i<=n :
    sum=sum+i
    i=i+1
print(sum)


"""Infinity
Outline:
Write a program to check the infinite loop?"""

i=0
while i<=0:
    print("I WILL RUN FOREVER")


"""Armstrong number
Outline:
Write a program to check if the number entered by the user is an Armstrong number or not?"""

num=int(input("Please enter a number:"))
sum=0
temp=num
while temp>0:
    sum=sum+((temp%10)**3)
    temp=temp//10
if sum==num:
    print("I am an armstrong number")
else:
    print("I am not an armstrong numer")


    
"""Harish was always fascinated by calenders and wanted to make one of
his own. He however did not have any programming knowledge to do
the same. He hired you to help with this program. He wants you to write
a program that displays the name of the day in a week whenever the
number of the day is given. The program should run multiple times till the
user asks the program to quit. Help him write the program to display the
day number and the name. (For ex. 1-Sunday, 2-Monday, 3-Tuesday
and so on till 7-Saturday). Use elif ladder and break statements
wherever needed."""  

while True:
    num=int(input("Enter a number:"))
    if num==1:
        print=("Sunday")
    elif num==2:
        print("Monday")
    elif num==3:
        print("Tuesday")
    elif num==4:
        print("Wednesday")
    elif num==5:
        print("Thursday")
    elif num==6:
        print("Friday")
    elif num==7:
        print("Saturday")
    elif num==8:
        break
    else:
        print("You do not know days of the week there are not more than 7 days.")
        
