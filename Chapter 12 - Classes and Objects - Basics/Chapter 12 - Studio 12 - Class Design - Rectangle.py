#  A rectangle has a length and a width. A rectangle should be able to provide
#  its area and perimeter. A rectangle can indicate whether it is smaller
#  than another rectangle in terms of area. A rectangle can indicate whether
#  it is in fact a square.


class Rectangle():

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_smaller(self, rect):
        return self.area() < rect.area()

    def is_a_square(self):
        return self.length == self.width

    def __repr__(self):
        __repr = '{"__Class": "Rectangle"' + ', ' + \
                 ' "__length": ' + str(self.length) + ',' + \
                 ' "__width": ' + str(self.width) + \
                 '}'
        return __repr


def my_test_equal(a, b):
    """ Home-rolled version of testEqual(a, b) """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of Rectangle Class """

    r1 = Rectangle(3, 10)
    r2 = Rectangle(5, 5)
    print(r1)
    print(r2)
    my_test_equal(r1.area(), 30)
    my_test_equal(r2.area(), 25)
    my_test_equal(r1.perimeter(), 26)
    my_test_equal(r2.perimeter(), 20)
    my_test_equal(r1.is_smaller(r1), False)
    my_test_equal(r1.is_smaller(r2), False)
    my_test_equal(r1.is_a_square(), False)
    my_test_equal(r2.is_a_square(), True)


if __name__ == "__main__":
    main()
