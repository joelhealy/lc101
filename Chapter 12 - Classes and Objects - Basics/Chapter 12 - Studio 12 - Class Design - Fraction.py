#  A fraction has a numerator and denominator. A fraction should be able to
#  add itself to another fraction, returning a new fraction that represents
#  the sum. A fraction should be able to multiply itself by another fraction,
#  returning a new fraction as the product. A fraction should be able to take
#  the reciprocal of itself, returning that value as a new fraction. A fraction
#  should be able to simplify itself, returning a new fraction as that
#  simplification.


def greatest_common_divisor(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b
    return a


class Fraction():

    def __init__(self, numerator, denominator):
        #  Simplify as part of the Constructor
        gcd = greatest_common_divisor(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def add(self, fract):
        return Fraction(fract.get_denominator() * self.numerator +
                        self.denominator * fract.get_numerator(),
                        fract.get_denominator() * self.denominator)

    def multiply(self, fract):
        return Fraction(self.numerator * fract.get_numerator(),
                        self.denominator * fract.get_denominator())

    def reciprocal(self):
        if self.denominator != 0:
            return Fraction(self.denominator, self.numerator)

    def simplify(self):
        gcd = greatest_common_divisor(self.numerator, self.denominator)
        return Fraction(self.numerator // gcd, self.denominator // gcd)

    def __repr__(self):
        __repr = '{"_Fraction__numerator": ' + str(self.numerator) + ',' + \
                 ' "_Fraction__denominator": ' + str(self.denominator) + \
                 '}'
        return __repr


def my_test_equal(a, b):
    """ Home-rolled version of testEqual(a, b) """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def my_test_for_none(result):
    """ Home-rolled test for None """

    if result is None:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of Fraction Class """

    f1 = Fraction(3, -10)
    f2 = Fraction(-5, 5)
    print(f1)
    print(f2)
    my_test_equal(str(Fraction(1, 2).add(Fraction(1, 3))), str(Fraction(5, 6)))
    my_test_equal(str(f1.multiply(f2)), str(Fraction(3, 10)))
    my_test_equal(str(f1.reciprocal()), str(Fraction(-10, 3)))
    my_test_for_none(Fraction(1, 0).reciprocal())
    my_test_equal(str(Fraction(1, 2).add(Fraction(3, 2)).simplify()),
                  str(Fraction(2, 1)))


if __name__ == "__main__":
    main()
