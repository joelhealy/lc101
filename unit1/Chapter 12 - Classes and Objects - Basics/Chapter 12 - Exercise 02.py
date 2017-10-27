#  Add a method reflect_x to the class Point which returns a new Point,
#  one which is the reflection of the point across the x-axis. For
#  example, Point(3, 5).reflect_x() is (3, -5)


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

    def reflect_x(self):
        return Point(self.get_x(), -self.get_y())

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def __str__(self):
        return "Point(" + str(self.get_x()) + ", " \
                        + str(self.get_y()) + ")"


def my_test_equal(a, b):
    """ Home-rolled version of testEqual() """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of Point.distance_from_point(point) """

    print(Point(3, 5))
    print("  when reflected should be: ")
    print(Point(3, 5).reflect_x())
    print()
    my_test_equal(Point(3, 5).reflect_x().__str__(), Point(3, -5).__str__())


if __name__ == "__main__":
    main()
