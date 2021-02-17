#Algebra solve 2x2 Equation
#ax+by = e
#cx+dy = f
#x = ed-bf/ad-bc, y = af-ec

a, b, c, d, e, f = eval(input("Enter value of a,b,c,d,e,f:"))

if((a*d)-(b*c)) == 0:
    print("Equation has no solution")
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)

    print("x is:", x, "and y is:", y)
