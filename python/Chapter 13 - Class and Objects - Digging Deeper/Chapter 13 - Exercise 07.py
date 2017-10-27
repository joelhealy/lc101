
#  Write a new method called diagonal that will return the length of the
#  diagonal that runs from the lower left corner to the opposite corner.


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

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def __str__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"


class Rectangle:

    def __init__(self, ll_corner_pt, width, height):
        """
        Create a new rectangle with lower left corner at point <ll_corner_pt>
        and having width <width> and height <height>
        """

        self.ll_corner_pt = ll_corner_pt
        self.width = width
        self.height = height

    def __repr__(self):
        return "ll_corner=" + str(self.ll_corner_pt) + ", " + \
               "width=" + str(self.width) + ", " + \
               "height=" + str(self.height)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def transpose(self):
        (self.width, self.height) = (self.height, self.width)

    def contains(self, point):
        ret_value = False
        x = point.get_x()
        y = point.get_y()
        x_min = self.ll_corner_pt.get_x()
        x_max = x_min + self.width
        y_min = self.ll_corner_pt.get_y()
        y_max = y_min + self.height
        if x_min <= x < x_max and y_min <= y < y_max:
            ret_value = True
        return ret_value

    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5


def my_test_approx_equal(a, b, c):
    """ Hand-rolled version of testEqual """

    if abs(a - b) < c:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of diagonal """

    r = Rectangle(Point(0, 0), 10, 5)
    my_test_approx_equal(r.diagonal(), 11.1803398875, 0.0000001)

    r1 = Rectangle(Point(0, 0), 12, 4)
    my_test_approx_equal(r1.diagonal(), 12.6491106407, 0.0000001)

    r2 = Rectangle(Point(0, 0), 1, 2)
    my_test_approx_equal(r2.diagonal(), 2.2360679775, 0.0000001)


if __name__ == "__main__":
    main()
