"""Sum of whole numbers
Outline:
Write a program to calculate the sum of whole numbers."""

n=int(input("Please enter the number you want to add:"))
sum=0

for i in range(1,n+1):
    sum=sum+i
print(sum)


"""Reverse a String
Outline:
Write a program to reverse the string entered by the user."""

string=input("Please enter your own string:")
string2=('')
for i in string:
    string2=i+string2
print(string)
print(string2)


"""reverse order
Outline:
Write a program to print the numbers in reverse order beginning from the number entered by the user."""

num=int(input("Please enter a number:"))
for i in range(num,0,-1):
    print(i)