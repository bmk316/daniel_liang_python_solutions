#QUESTION 2.14
# Area of a Triangle

x1, y1 = eval(input("Enter the first pair of points:"))
x2, y2 = eval(input("Enter the second pair of points:"))
x3, y3 = eval(input("Enter the third pair of points:"))

area = round(abs(0.5*(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))),2)
print("Area of the triangle is: ", area)