#QUESTION 2.25

import turtle

centerX = float(input("Enter the center x cordinates of the rectangle: "))
centerY = float(input("Enter the center y cordinates of the rectangle: "))
width = float(input("enter, width: "))
height = float(input("enter, height: "))

turtle.showturtle()

turtle.penup()
turtle.goto(centerX-width/2,centerY-height/2)
turtle.pendown()
turtle.goto(centerX-width/2,centerY+height/2)
turtle.goto(centerX+width/2,centerY+height/2)
turtle.goto(centerX+width/2,centerY-height/2)
turtle.goto(centerX-width/2, centerY-height/2)

turtle.done()