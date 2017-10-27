#  Write a new method called contains in the Rectangle class to test if a
#  Point falls within the rectangle. For this exercise, assume that a
#  rectangle at (0,0) with width 10 and height 5 has open upper bounds on the
#  width and height, i.e. it stretches in the x direction from [0 to 10),
#  where 0 is included but 10 is excluded, and from [0 to 5) in the y
#  direction. So it does not contain the point (10, 2).


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


def my_test_equal(a, b):
    """ Hand-rolled version of testEqual """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of contains """

    r = Rectangle(Point(0, 0), 10, 5)
    my_test_equal(r.contains(Point(0, 0)), True)
    my_test_equal(r.contains(Point(3, 3)), True)
    my_test_equal(r.contains(Point(3, 7)), False)
    my_test_equal(r.contains(Point(3, 5)), False)
    my_test_equal(r.contains(Point(3, 4.99999)), True)
    my_test_equal(r.contains(Point(-3, -3)), False)


if __name__ == "__main__":
    main()
