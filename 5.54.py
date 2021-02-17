import turtle as t
import math

t.showturtle()
t.backward(180)
t.forward(360)
t.stamp()
t.backward(180)
t.left(90)
t.forward(100)
t.stamp()
t.backward(200)
t.forward(100)
t.right(90)
t.backward(180)

t.penup()
t.goto(-100,100)
t.pendown()
for x in range (-100, 100):
    t.goto(x, 0.01*(x**2))
t.hideturtle()
t.done()