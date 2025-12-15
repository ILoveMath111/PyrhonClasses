"""Overload Operators
Outline:
Write a program to overload the less than (<) and equal to (==) operators.
For example, create objects - ob1 and ob2 with values 3 and 4 to compare values, respectively.
You can additionally create more objects to try different values."""

class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if(self.a<other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
    def __eq__(self,other):
        if(self.a==other.a):
            return "Both are equal"
        else:
            return "Not equal"
ob1=A(2)
ob2=A(3)
print("Passed Values:",ob1.a,ob2.a)
print(ob1<ob2)
ob3=A(4)
ob4=A(4)
print("Passed Values:",ob3.a,ob4.a)
print(ob3==ob4)



class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+' ( '+self.meaning+' )'
flash=[]
print("Welcome to flashcard application")
while(True):
    word= input("Enter the name of the word you would like to add to flashcard:")
    meaning= input("Enter the meaning of the word you picked:")
    flash.append(flashcard(word,meaning))
    option= int(input("Please enter 0 if you want to add another flashcard, or enter one to end the game:"))
    if(option):
        break
print("\nYour flashcards")
for i in flash:
    print(">",i)



"""Fruit Quiz
Outline:
Write a program to create a quiz related to multiple fruits using object-oriented programming in Python.
Create a class that consists of - 1. a constructor with a dictionary of fruits and respective colours 2. a function to execute the quiz.
Here, the fruit will be chosen at random from the dictionary. Then ask the user to enter the colour of that fruit.
Evaluate the answer and display the result accordingly."""

import random
class FruitQuiz:
    def __init__(self):
        self.fruits={'apple':'red','lemons':'yellow','tomatoes':'red','orange':'orange'}
    def quiz(self):
        while(True):
            fruit, color=random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
            user_answer=input()
            if(user_answer.lower()==color):
                print("Correct answer")
            else:
                print("Wrong answer")
            option=int(input("Please enter 0 if you would like to play again, if not enter 1:"))
            if (option):
                break
print("Welcome to the fruit quiz")
fq=FruitQuiz()
fq.quiz()