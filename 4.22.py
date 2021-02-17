#4.22 Geometrey problem

import math

x,y = eval(input("Enter your coordinates: "))

c1,c2 = 0,0
radius = 10

distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

if distance <= 10:
    print("Points are inside the circle")

else :
    print("Points are outside the circle")

