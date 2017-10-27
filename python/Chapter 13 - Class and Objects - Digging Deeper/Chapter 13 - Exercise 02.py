
#  Add the following accessor methods to the Rectangle class: get_width and
#  get_height.


class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x_

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


def main():
    """ Cursory test of Rectangle class """

    loc = Point(4, 5)
    r = Rectangle(loc, 6, 5)
    print(r)
    print("Height of r =", r.get_height())
    print("Width of r =", r.get_width())


if __name__ == "__main__":
    main()
