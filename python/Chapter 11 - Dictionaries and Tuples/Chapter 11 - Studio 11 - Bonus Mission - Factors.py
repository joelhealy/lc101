#  Create a function factors that takes in an integer n and generates a
#  dictionary that contains the factors of all values from 1 to n. A factor
#  is any number that evenly divides another number. For example, the factors
#  of 6 are 1, 2, 3, and 6. Factors of 15 are 1, 3, 5, and 15. The keys of
#  your dictionary should be an integer between 1 and n and the values should
#  be a list of factors for that particular key.


def factors(n):
    """ Return a dictionary of factors of all values from 1 to <n>. """

    factors_dict = {}
    for key in range(1, n + 1):
        factors_dict[key] = []
        for factor in range(1, key + 1):
            if key % factor == 0:
                factors_dict[key].append(factor)
    return factors_dict


def my_test_equal(a, b):
    """ Home-rolled version of testEqual(a, b) """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of factors(n) """

    my_test_equal(factors(6),
                  {1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2, 4],
                   5: [1, 5], 6: [1, 2, 3, 6]})


if __name__ == "__main__":
    main()
