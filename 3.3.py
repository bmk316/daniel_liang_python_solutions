#QUESTION 3.3
#GPS COORDINATES
import math
#ATLANTA
x1 = 33.7490
y1 = -84.3880
#ORLANDO, FLORIDA
x2 = 28.5383
y2 = -81.3792
#CHARLOTTE, NC
x3 = 35.2271
y3 = -80.8431
#SAVANNAH, GA
x4 = 32.0809
y4 = -81.0912

#compute d1,d2,d3,d4 (sides of the quadrilateral including the diagonal)
radius = 6371.01

d1 = radius * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) \
     + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos((math.radians(y1) - math.radians(y2))))

d2 = radius * math.acos(math.sin(math.radians(x2)) * math.sin(math.radians(x3)) \
     + math.cos(math.radians(x2)) * math.cos(math.radians(x3)) * math.cos((math.radians(y2)-math.radians(y3))))

d3 = radius * math.acos(math.sin(math.radians(x3)) * math.sin(math.radians(x4)) \
     + math.cos(math.radians(x3)) * math.cos(math.radians(x4)) * math.cos((math.radians(y3) - math.radians(y4))))

d4 = radius * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x4)) \
     + math.cos(math.radians(x1)) * math.cos(math.radians(x4)) * math.cos((math.radians(y1) - math.radians(y4))))

d5_diagonal = radius * math.acos(math.sin(math.radians(x3)) * math.sin(math.radians(x4)) \
     + math.cos(math.radians(x3)) * math.cos(math.radians(x4)) * math.cos((math.radians(y3) - math.radians(y4))))


s1 = (d1+d2+d5_diagonal)/2
area_1 = math.sqrt(s1*(s1-d1)*(s1-d2)*(s1-d5_diagonal))
print("Area 1:", area_1)
s2 = (d3+d4+d5_diagonal)/2
area_2 = math.sqrt(s2*(s2-d3)*(s2-d4)*(s2-d5_diagonal))
print("Area 2:", area_2)

# print("Total Area is Area 1 + Area 2 = " + str(area_1+area_2) + " KM2")
print("Total Area is Area 1 + Area 2 = {} KM\u00b2".format(str(area_1 + area_2)))





