# Use the functions defined in Listing 6.14 to write a program that displays a
# rectangle centered at (- 75, 0)
# with width and height 100 and a circle centered at (50, 0) with radius 50.
# Fill 10 random points inside the rectangle and 10 inside the circle

import random
import turtle

def drawPoint(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()

def drawCircle(x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)


def drawRectangle(x, y, width, height):
    turtle.penup()
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)


def main():
    drawRectangle(-75, 0, 100, 100)
    drawCircle(50, 0, 50)
    turtle.speed(5)
    for i in range(10):
        drawPoint(random.randint(-115, -30), random.randint(-50, 40))
        drawPoint(random.randint(20, 90), random.randint(-40, 25))
    turtle.done()

main()


# import turtle as t
# import math
# import random
#
# def drawCircle(x=50, y=0, radius=50):
#     t.showturtle()
#     t.penup()
#     t.goto(x,y-radius)
#     t.pendown()
#     t.circle(radius)
#
# def drawRectangle(x=-75, y=0, height=100, width=100):
#
#     t.penup()
#     t.goto(x+width/2, y+height/2)
#     t.pendown()
#     t.right(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(width)
#     t.right(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(width)
#     t.done()
#
# def main():
#     circle_x = ''
#     circle_y = ''
#     radius_circle = ''
#     drawCircle(circle_x, circle_y,radius_circle)
#     drawRectangle()
#
# main()