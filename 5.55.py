from turtle import *


def draw_square():

    for l in range(4):
        showturtle()
        forward(30)
        left(90)

    forward(30)

up()

speed(6)

for i in range(8):
    up()
    setpos(0, 30*i) # start with zero-th row first
    down()

    for j in range(8):
        if (i+j) % 2 == 0: #alternating color logic and zeroth row+1, zeroth row+2 ....zeroth row+7
            col = "black"
        else:
            col = "white"

        fillcolor(col)
        begin_fill()
        draw_square() #Draw-the-squares
        end_fill()

done()