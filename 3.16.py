import turtle
#TRIANGLE

turtle.showturtle()
turtle.fillcolor("light grey")
turtle.begin_fill()
turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.left(60)
turtle.circle(50,steps = 3)
turtle.end_fill()

#SQUARE

turtle.fillcolor("blue")
turtle.begin_fill()
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
turtle.right(15)
turtle.circle(50,steps = 4)
turtle.end_fill()

#PENTAGON
turtle.fillcolor("magenta")
turtle.begin_fill()
turtle.penup()
turtle.goto(20,0)
turtle.pendown()
turtle.right(10)
turtle.circle(50,steps = 5)
turtle.end_fill()

#HEXAGON
turtle.fillcolor("green")
turtle.begin_fill()
turtle.penup()
turtle.goto(130,0)
turtle.pendown()
turtle.right(5)
turtle.circle(50,steps = 6)
turtle.end_fill()

#HEPTAGON
turtle.fillcolor("grey")
turtle.begin_fill()
turtle.penup()
turtle.goto(250,0)
turtle.pendown()
turtle.right(5)
turtle.circle(50,steps = 7)
turtle.end_fill()

turtle.done()