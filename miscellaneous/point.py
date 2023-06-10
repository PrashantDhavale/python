import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x__ = x
        self.__y__ = y

    def getx(self):
        return self.__x__

    def gety(self):
        return self.__y__

    def distance_from_xy(self, x, y):
        h = math.hypot(x, y, self.getx(), self.gety())
        return h

    def distance_from_point(self, point):
        h = self.distance_from_xy(point.getx(), point.gety())
        return h


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
