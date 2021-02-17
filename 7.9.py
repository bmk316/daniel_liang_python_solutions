#INTERSECING LINES PROGRAM
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

    program = LinearEquation(9, 4, 3, -5, -6, -21)

    if program.isSolvable():
        print("Value of x is:", program.getX())
        print("Value of y is:", program.getY())

    else:
        print("Equation has no solutions")