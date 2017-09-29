#  Write a function sum_of_squares(xs) that computes the sum of the squares of
#  the numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should
#  return 4+9+16 which is 29:


def sum_of_squares(xs):
    """ Return the sum of the squares of the items in <xs>"""

    sum = 0
    for x in xs:
        sum += x * x
    return sum


def testEqual(a, b):
    """ Home-rolled testEqual """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of sum_of_squares(xs) """

    testEqual(sum_of_squares([2, 3, 4]), 29)


if __name__ == "__main__":
    main()
