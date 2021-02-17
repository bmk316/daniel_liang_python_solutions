#SINE and #COSINE

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

for i in range (-180, 181):
    t.pencolor("red")
    t.goto(i,math.sin(math.radians(i))*100)

t.penup()
t.goto(-180,0)

t.goto(-180,math.cos(math.radians(-180))*100)
t.pendown()
for i in range (-179, 181):
    t.pencolor("blue")
    t.goto(i, math.cos(math.radians(i)) * 100)

t.done()
