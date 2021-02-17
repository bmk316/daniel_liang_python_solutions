import turtle as t

x1, y1 = map(int,input("Enter first set of points:").strip().split(" "))
# x1, y1 = eval(input("Enter first set of points:"))
x2, y2 = map(int,input("Enter second set of points:").strip().split(" "))

t.showturtle()
t.penup()
t.goto(x1,y1)
t.write("("+str(x1)+","+str(y1)+")")
t.pendown()
t.goto(x2,y2)
t.write("("+str(x2)+","+str(y2)+")")

t.done()