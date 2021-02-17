class Point:
    def _init_(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distance(self,P):
        d = ((self.__x-P.getX())**2+(self.__y-P.getY())**2)**0.5
        return d

    def isNear(self,P):
        if self.distance(P) < 5:
            print("The points are near each other")
        else:
            print("The points are not near each other")

def main():
    x1, y1, x2, y2=eval(input("Enter the points x1,y1,x2,y2 "))
    P1 = Point(x1,y1)
    P2 = Point(x2,y2)

    print("The distance between the two points is", P1.distance(P2))
    P1.isNear(P2)

main()
