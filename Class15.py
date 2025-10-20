"""Well wishes
Outline:
Write a program to create a function name well wishes that will give output hello,
 how are you!"""

def wellwishes():
    print("Hello how are you,it is very nice to meet you.")

wellwishes()



"""Weather condition
Outline:
Write a program to display the weather in autumn and spring :"""

def weather():
    print("The weather in spring is very pleasant")
    print("The weather is autum is cold and harsh")
spring="autum"
autum=spring
weather()



"""Calculator
Outline:
Write a program to make a calculator : For 
making a calculator create four functions add, subtract,
 multiply, divide. Ask for a choice from users which operation
 they want to perform. Take user input whatever operation
 they want to perform And call that function accordingly."""

def add(P,Q):
    return P+Q
def subract(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q
def divide(P,Q):
    return P/Q
print("Please select the operation")
print("a. Add")
print("b. Subract")
print("c. Multiply")
print("d. Divide")
choice=input("Please enter choice (a/b/c/d):")
num1=int(input("Please enter the first number:"))
num2=int(input("Please enter the econd number:"))
if choice=='a':
    print("The sum of your numbers are",add(num1,num2))
elif choice=='b':
    print("The difference of your numbers are",subract(num1,num2))
elif choice=='c':
    print("The product of your numbers are",multiply(num1,num2))
elif choice=='d':
    print("The quotient of your numbers are",divide(num1,num2))
else:
    print("This is an invalid input")