# EXERCISE 12.1 from GeometricObject import GeometricObject


class TriangleError(RuntimeError):

    def __init__(self, side1, side2, side3):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def setSide1(self, side1):
        self.__side1 = side1

    def getSide2(self):
        return self.__side2

    def setSide2(self, side2):
        self.__side2 = side2

    def getSide3(self):
        return self.__side3

    def setSide3(self, side3):
        self.__side3 = side3

    def isAllowed(self):
        return self.__side1 + self.__side2 > self.__side3 and \
               self.__side2 + self.__side3 > self.__side1 and \
               self.__side1 + self.__side3 > self.__side2

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def getArea(self):
        if not self.isAllowed():
            raise TriangleError(self.__side1, self.__side2, self.__side3)

        p = self.getPerimeter()
        area = (p * (p - self.__side1) * (p - self.__side2) * (p - self.__side3)) ** 0.5

        return area


def main():
    try:
        side1, side2, side3 = eval(input("Enter the three sides of a Triangle: "))
        # color = input("Enter the color of Triangle: ")
        # isFilled = eval(input("Is Triangle filled(0/1): "))

        T = TriangleError(side1,side2,side3)
        # T.setColor(color)
        # T.setFilled(isFilled)

        print("Area is: ", T.getArea()," and Perimeter is: ", T.getPerimeter())
        # " Color is:", T.getColor(),
        #       " Filled: ", str(T.isFilled()))

    except TriangleError:
        print("It's an invalid triangle")


main()

# class Triangle(GeometricObject):
#     def __init__(self, side1=1.0, side2=1.0, side3=1.0):
#         super().__init__()
#         self.__side1 = float(side1)
#         self.__side2 = float(side2)
#         self.__side3 = float(side3)
#
#     def getSide1(self):
#         return self.__side1
#
#     def setSide1(self, side1):
#         self.__side1 = side1
#
#     def getSide2(self):
#         return self.__side2
#
#     def setSide2(self, side2):
#         self.__side2 = side2
#
#     def getSide3(self):
#         return self.__side3
#
#     def setSide3(self, side3):
#         self.__side3 = side3
#
#     def getPerimeter(self):
#         return (self.__side1 + self.__side2 + self.__side3)
#
#     def getArea(self):
#         p = self.getPerimeter()
#         area = (p * (p - self.__side1) * (p - self.__side2) * (p - self.__side3)) ** 0.5
#         return area
#
#     def __str__(self):
#         return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) \
#                    + " side3 = " + str(self.__side3)