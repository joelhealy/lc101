#  Sum up all the negative numbers in a list


def sum_of_negs(xs):
    """ Return the sum of all of the negative items in <xs>"""

    sum = 0
    for x in xs:
        if x < 0:
            sum += x
    return sum


def testEqual(a, b):
    """ Home-rolled testEqual """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of sum_of_negs(xs) """

    testEqual(sum_of_negs([2, 3, 4]), 0)
    testEqual(sum_of_negs([6, -5, -2, 3]), -7)
    testEqual(sum_of_negs([-2, -3, -4]), -9)
    testEqual(sum_of_negs([-2.5, 3, -4.2]), -6.7)


if __name__ == "__main__":
    main()
