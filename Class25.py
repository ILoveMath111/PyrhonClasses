"""Hands-on Map
Outline:
Write a program to return the addition of numbers of two different lists. Then, display a list that is
square of numbers of another list. Use the map() function here to get the desired result."""

# Add two lists using map and lambda
numbers1=[1,2,3]
numbers2=[4,5,6]
result=map(lambda x,y:x+y,numbers1,numbers2)
print("Additon of two lists")
print(list(result))

# Using map
nums=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq,nums))
print("Square of numbers in list")
print(square)



"""Zip It!
Outline:
Write a program to return - 1. zipped list from two lists 2. 
Elements of two lists zipped together, but 2nd list in reverse order 3. elements of two lists zipped into a dictionary"""

# Zip elements of two lists
s1={2,3,1}
s2={'b','a','c'}
s3=list(zip(s1,s2))
print(s3)

# Zip elements of two lists
list1=[10,20,30,40]
list2=[100,200,300,400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)

# Zip into dictionary
stocks=['reliance','infosys','tcs']
prices=[2175,1127,2750]
new_dict={stocks: prices for stocks,prics in zip(stocks,prices)}
print('\n{}'.format(new_dict))



"""That’s the exit
Outline:
Write a program where the value of i begins from 1 and goes to 10. When the value of i becomes 5, force the interpreter to exit the program."""

for i in range(10):
    if i==5:
        print(exit)
        exit()
    print(i)