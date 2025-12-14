"""Abstract Class
Outline:
Write a program to create a base class that consists of two functions - one to display a value, and another
function is an abstract method. Next, create a subclass that consists of a method similar to the abstract
method. Finally, showcase how Abstraction is being implemented in this example."""

from abc import ABC,abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value:",x)
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")
class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")
test_obj=test_class()
test_obj.task()
test_obj.print(100)



"""Class Animal
Outline:
Write a program to implement abstraction on animal class (base class). The abstract method will be move will display what subclasses can do.
Subclasses can be something like - Human, Dog."""

from abc import ABC,abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Snake(Animal):
    def move(self):
        print("I can slither")
class Dog(Animal):
    def move(self):
        print("I can bark")
class Lion(Animal):
    def move(self):
        print("I can roar")
R=Human()
R.move()
K=Snake()
K.move()
R=Dog()
R.move()
K=Lion()
K.move()



"""All about Countries
Outline:
Write a program to create two classes for two different countries that consist of three methods to display the following information of
respective country - capital, language and type of country. Then, use Polymorphism to create a common interface for both classes."""

class India():
    def capital(self):
        print("New Delhi is the capital of India ")
    def language(self):
        print("Hindi is the most widley spoken language of India")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("Washington,D.C. is the capital of USA")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is a developed country")
obj_ind=India()
obj_usa=USA()
for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()



# Extra thing for me to do

class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Meow")
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Bark")
cat1=Cat("Kitty",2.5)
dog1=Dog("Fluffy",4)
for animal in (cat1,dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()