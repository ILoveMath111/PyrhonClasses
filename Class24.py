"""Operations on Sets
Outline:
Write a program to create a set and perform the following operations on that set- 1.
Create a set with integer elements 2. Create a set with mixed data type elements 3.
Create another set with elements - 1, 2, 3, 4, 3, 2 4.
Create a set from a list with elements - [1, 2, 3, 2] 5.
Print the set after removing the first element from this set - [0, 1, 3, 4, 5]"""

# Different types of sets in python
my_set={1,2,3}
print(my_set)
# Set of mixed datatypes
my_set1={1.0,"Hello",(1,2,3)}
print(my_set1)
# Set cannot have duplicates
my_set={1,2,3,4,3,2}
print(my_set)
# Remove a number from a set
num_set=set({0,1,3,4,5})
print("Original set:")
print(num_set)
num_set.pop()
print("After removing the first element from the said set:")
print(num_set)



"""Set Intersection
Outline:
Write a program to find the intersection of two sets. Set1 = {green, blue} Set2 = {blue, yellow}"""

setx={"green","blue"}
sety={"blue","yellow"}
print("Original set of elements:")
print(setx)
print(sety)
print("Intersection of two said sets:")
setz=setx.intersection(sety)
print(setz)



"""Arrays
Outline:
Write a program to create an array with the following elements - [1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the
 array. Also, print the reversed array."""

import array as arr
array_num=arr.array('i',[1,3,5,3,7,9,3])
print("Original array:"+str(array_num))
print("Number of occurences of the number 3 in the said array:"+str(array_num.count(3)))
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))