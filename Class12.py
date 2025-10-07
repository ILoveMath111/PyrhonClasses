"""Character occurrence
Outline:
Write a program to check how many times a character is repeated in a word?"""

string=input("Enter a string :")
char=input("Enter a character:")
i=0
count=0
while (i<len(string)):
    if (string[i]==char):
        count=count+1
    i=i+1
print("The total number of times",char,"has occured=",count)


"""Is this a Prime Number
Outline:
Write a program to print all the prime numbers which come in the range entered by the user?"""

upper=int(input("Enter the value of upper:"))
lower=int(input("Enter the value of lower:"))
print("Prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num % i)==0:
                break
        else:
            print(num)



"""Mid product
Outline:
Write a program to calculate the product of the middle digits of a number?"""

#Input a number 
num = int(input("Enter the number : "))
t = num
numLen = 0
#iterate the loop
while t>0: 
  numLen = numLen+1
  t = int(t/10)

if numLen>=4: #condition 1
  numLen = int(numLen/2)
  chk = 0
  while num>0: #iterate loop
    rem = num%10
    if chk==numLen: #nested condition 1
      midOne = rem
    elif chk==(numLen-1): 
      midTwo = rem
    num = int(num/10)
    chk = chk+1
  prod = midOne*midTwo #product of middle digits
  #display the result
  print("\nProduct of Mid digits (" +str(midOne)+ "*" +str(midTwo)+ ") = ", prod)

else:
  print("\nIt's not a 4 or more than 4-digit number!")