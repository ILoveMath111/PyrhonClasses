"""Break
Outline:
Write a program to check alphabet “A” is present in the given string or not.
And terminate the loop after finding the alphabet “A."""

a=input("Enter a word:")
for i in a:
    if (i=='A' or i=='a'):
        print("A is found")
        break
    else:
        print("A not found",i)



"""Continue
Outline:
Write a program to display 1 to 10 numbers in reverse order and skip the number 5."""

for i in range(10,0,-1):
    if i==10:
       continue
    print(i)



    """Pass
Outline:
Write a program to satisfy the following conditions of the given range: If the number is divisible by 20, it provides an output "twist."
If the number is divisible by 15, it will pass (no output) If the number is divisible by 5, it will give an output “fizz.” If the number is
divisible by 3, it will give an output "buzz."
Otherwise, it will give the output of that number."""

num=int(input("Please enter a number:"))
if num%20==0:
    print("twist")
elif num%15==0:
    pass
elif num%5==0:
    print("fizz")
else:
    print(num)