#This is my example
"""import turtle
turtle.Screen()
turtle.Screen().setup(600,600)
a=turtle.Turtle()
a.forward(100)
a.left(90)
a.forward(100)
a.right(90)
a.forward(100)
a.penup()
a.goto(100,200)
a.pendown()
a.backward(100)
turtle.done()"""



"""Polygon
Outline:
Write a program to set screen size, colour for turtle graphics and draw a polygon using turtle?

import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
numsides=6
sidelength=70
angle=360.0/numsides
for i in range(numsides):
    polygon.forward(sidelength)
    polygon.right(angle)
turtle.done()"""



"""Star
Outline:
Write a program to draw a star using a turtle?

import turtle
turtle.Screen().bgcolor("Aqua")
board=turtle.Turtle()
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
board.penup()
board.right(150)
board.forward(50)
board.pendown()
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)
turtle.done()"""



import turtle
mywn=turtle.Screen()
mywn.bgcolor("light blue")
mywn.title("Turtle")
mypen=turtle.Turtle()
size=0
while True:
    for i in range(4):
        mypen.fd(size+1)
        mypen.left(90)
        size=size-5
    size=size+1
turtle.done()