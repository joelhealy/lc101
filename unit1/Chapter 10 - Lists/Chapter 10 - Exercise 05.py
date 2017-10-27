#  Write a Python function that will take a list of 100 random integers
#  between 0 and 1000 (you can use iteration, append, and the random module
#  to create a test list) and return the maximum value. (Note: there is a
#  built-in function named max but do not use it for this exercise.)

import random


def max_int_in_list(list_of_ints):
    """
    Return the largest item in <list_of_ints>
    Note: <list_of_ints> must contain at least one element
    """
    maxint = list_of_ints[0]
    for i in list_of_ints:
        if i > maxint:
            maxint = i
    return maxint


def list_of_random_ints(low, high, length):
    """
    Return a list of <length> random integers between <low> and <high>
    (<low> is included in the range, but <high> is excluded)
    """

    list_of_ints = []
    for _ in range(length):
        list_of_ints.append(random.randrange(low, high))
    return list_of_ints


def main():
    """ Cursory test of max_int_in_list(list_of_ints) """

    low = 0
    high = 1000
    length = 100
    my_list = list_of_random_ints(low, high, length)
    print("Largest int in list of", len(my_list),
          "random ints between", low, "and", high, "is",
          max_int_in_list(my_list))


if __name__ == "__main__":
    main()
