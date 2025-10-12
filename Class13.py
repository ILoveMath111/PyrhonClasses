"""Right angle triangle
Outline:
Write a program to demonstrate a right angle triangle pattern?"""

print("Half pyramid pattern of stars(*):")
n=int(input("Enter number of rows:"))
for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print()



"""Floyd’s triangle
Outline:
Write a program to demonstrate a Floyd triangle pattern?"""

rows=int(input("Enter number of rows:"))
number=1
print("Floyd's triangle")
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(number,end=' ')
        number=number+1
    print()



"""Diamond Pattern
Outline:
Write a program to demonstrate the numbers in a diamond pattern?"""

rowSize=int(input("What is the number of rows:"))
if rowSize%2==0:
    halfDiamRow=int(rowSize/2)
else:
    halfDiamRow=int(rowSize/2)+1
space=halfDiamRow-1
for i in range(1,halfDiamRow+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()
space=1
for i in range(1,halfDiamRow):
    for j in range(1,space+1):
        print(end=" ")
    space=space+1
    num=1
    for j in range(1,2*(halfDiamRow-i)):
        print(end=str(num))
        num=num+1
    print()