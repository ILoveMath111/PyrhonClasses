"""Tuple Operations
Outline:
Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create
another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4.
Count the occurrences of an element in the tuple 5. Perform slicing on the tuple"""

tuplex=("tuple",False,3.2,1)
print(tuplex)
tuplex1=(4,6,2,8,3,1)
print(tuplex1)
tuplex2=tuplex1+(9,)
print(tuplex2)
tuple1=(50,10,60,70,50)
print(tuple1.count(50))
tuplex3=(2,4,3,5,4,6,7,8,6,1)
_slice=tuplex3[3:5]
print(_slice)
_slice=tuplex3[:6]
print(_slice)



"""Flip Flop
Outline:
Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. 
If it's a palindrome, then it is the same after being reversed."""

def palind(r):
    e=len(r)-1
    s=0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r=(1,2,3,3,2,1)
if(palind(r)):
    print("The tuple is Flip-Flop")
else:
    print("The Tuple is not Flip-Flop")



"""Weather Prediction
Outline:
Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0). If the element is 1 then the value of rainy increases by 1 otherwise
 the value of sunny increases by 1. On the basis of the value of rainy and sunny, predict the weather."""

weather=(1,0,0,0,1,1,0)
sunny=0
rainy=0
for i in range(0,7):
    if(weather[i]==0):
        rainy+=1
    else:
        sunny+=1
if(sunny>rainy):
    print("Good weather")
else:
    print("Bad weather")