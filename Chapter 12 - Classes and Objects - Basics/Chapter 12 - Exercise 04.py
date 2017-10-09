#  Add a method called move that will take two parameters, call them dx and dy.
#  The method will cause the point to move in the x and y direction the number
#  of units given. (Hint: you will change the values of the state of the point)


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

    def move(self, dx, dy):
        """
        Move the Point <dx> units in the x direction and <dy> units in the y
        direction.
        """

        self.x += dx
        self.y += dy


def my_test_equal(a, b):
    """ Home-rolled version of testEqual """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of Point.move() """

    p1 = Point(3, 2)
    p1.move(4, -6)
    my_test_equal(p1.get_x(), 7)
    my_test_equal(p1.get_y(), -4)


if __name__ == "__main__":
    main()
