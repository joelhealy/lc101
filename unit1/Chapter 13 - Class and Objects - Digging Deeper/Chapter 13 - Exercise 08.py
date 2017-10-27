#  There are some games where we put a rectangular “bounding box” around our
#  sprites in the game. We can then do collision detection between, say, bombs
#  and spaceships, by comparing whether their rectangles overlap anywhere.
#
#  Write a function to determine whether two rectangles collide. Hint: this
#  might be quite a tough exercise! Think carefully about all the cases as
#  you code.


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

    def corners(self):
        """ Return a list of the four corner points """

        llcp = self.ll_corner_pt
        # include Lower Left corner pt
        corner_list = [llcp]
        # include Upper Left corner pt
        corner_list.append(
            Point(
                llcp.get_x(),
                llcp.get_y() + self.get_height()))
        # include Lower Right corner pt
        corner_list.append(
            Point(
                llcp.get_x() + self.get_width(),
                llcp.get_y()))
        # include Upper Right corner pt
        corner_list.append(
            Point(
                llcp.get_x() + self.get_width(),
                llcp.get_y() + self.get_height()))
        return corner_list

    def collision(self, rect):
        collision_occurred = False
        for corner in self.corners():
            if rect.contains(corner):
                collision_occurred = True
        for corner in rect.corners():
            if self.contains(corner):
                collision_occurred = True
        return collision_occurred


def my_test_equal(a, b):
    """ Home-rolled version of testEqual() """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of collision(r1, r2) """

    r1 = Rectangle(Point(0, 0), 10, 5)
    r2 = Rectangle(Point(2, 2), 10, 5)
    r3 = Rectangle(Point(100, 100), 10, 5)
    my_test_equal(r1.collision(r2), True)
    my_test_equal(r1.collision(r3), False)


if __name__ == "__main__":
    main()
