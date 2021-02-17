import math

class RegularPolygon:
    def __init__(self, n=3, side=1.0, x=0.0, y=0.0):

        self.__n = int(n)
        self.__side = float(side)
        self.__x = float(x)
        self.__y = float(y)

    # Getters (Accessors)

    def getn(self):
        return self.__n

    def getSide(self):
        return self.__side

    def x_coordinate(self):
        return self.__x

    def y_coordinate(self):
        return self.__y

    # Setters(Accessors)

    def setn(self, n):
        self.__n = int(n)

    def setSide(self, side):
        self.__side = float(side)

    def x_coordinate(self, x):
        self.__x = float(x)

    def y_coordinate(self, y):
        self.__y = float(y)

    def getPerimeter(self):
        return self.__n * self.__side

    def getAreaPolygon(self):
        return (self.__n * self.__side**2)/(4*math.tan(math.pi/self.__n))

def main():

    R0 = RegularPolygon()
    print("Perimeter of first Polygon is: ", R0.getPerimeter(), "units")
    print(f"Area of first Polygon Polygon is: {R0.getAreaPolygon():,.2f} sq.units\n")
    R1 = RegularPolygon(6,4)
    print("Perimeter of second Polygon is: ", R1.getPerimeter(), "units")
    print(f"Area of second Polygon Polygon is: {R1.getAreaPolygon():,.2f} sq.units\n")
    R2 = RegularPolygon(10, 4, 5.6, 7.8)
    print("Perimeter of third Polygon is: ", R2.getPerimeter(), "units")
    print(f"Area of third Polygon Polygon is: {R2.getAreaPolygon():,.2f} sq.units")

main()
