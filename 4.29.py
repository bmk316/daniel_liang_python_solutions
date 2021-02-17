#4.29 Radii of two circles and overlapping

import math

r1 = eval(input("Enter radius of circle1:"))
r2 = eval(input("Enter radius of circle2:"))

x1,y1 = eval(input("Enter centre co-ordinates of circle1:"))
x2,y2 = eval(input("Enter centre co-ordinates of circle2:"))

distance_between_radii = abs(r1-r2)
distance_between_centres = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))

if distance_between_centres <= distance_between_radii:
    print("Circle 2 is inside Circle 1")

elif distance_between_centres <= (r1+r2):
    print("Circle 2 overlaps Circle 1")