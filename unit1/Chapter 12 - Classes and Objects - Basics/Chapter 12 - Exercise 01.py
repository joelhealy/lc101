#  Add a distance_from_point method that works similar to
#  distance_from_origin except that it takes a Point as a
#  parameter and computes the distance between that point
#  and self.


class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distance_from_point(self, point):
        dx = self.x - point.get_x()
        dy = self.y - point.get_y()
        return ((dx ** 2) + (dy ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


def my_test_equal(a, b):
    """ Home-rolled version of testEqual() """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of Point.distance_from_point(point) """

    p1 = Point(1, 2)
    p2 = Point(4, -2)
    my_test_equal(p1.distance_from_point(p2), 5)
    my_test_equal(p2.distance_from_point(p1), 5)
    my_test_equal(p1.distance_from_point(p1), 0)


if __name__ == "__main__":
    main()
