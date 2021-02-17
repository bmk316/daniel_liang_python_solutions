#LINEAR EQUATION

class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

  # Getters (Accessors)

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getD(self):
        return self.__d

    def getE(self):
        return self.__e

    def getF(self):
        return self.__f

    def isSolvable(self):
        if (self.__a * self.__d) - (self.__b * self.__c) == 0:
            return False
        else:
            return True

    def getX(self):
        x = ((self.__e * self.__d) - (self.__b * self.__f)) / ((self.__a * self.__d) - (self.__b * self.__c))
        return x

    def getY(self):
        y = ((self.__a * self.__f) - (self.__e * self.__c)) / ((self.__a * self.__d) - (self.__b * self.__c))
        return y


def main():

    x1, y1, x2, y2 = eval(input("Enter the endpoints of the first line segment: "))

    a1 = y1 - y2
    b1 = x2 - x1
    e1 = -(x1 * y2 - x2 * y1)

    x3, y3, x4, y4 = eval(input("Enter the endpoints of the second line segment:"))
    c1 = y3 - y4
    d1 = x4 - x3
    f1 = -(x3 * y4 - x4 * y3)

    program = LinearEquation(a1,b1,c1,d1,e1,f1)

    if program.isSolvable():
        print("The intersecting pont is: (", program.getX(),",",program.getY(), ")")

    else:
        print("No intersecting point!")


main()

