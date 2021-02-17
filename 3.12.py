import turtle

length = eval(input("Enter length of star: "))
turtle.showturtle()
for i in range(5):
    turtle.forward(length)
    turtle.right(144)
turtle.done()