#  Write a function to count how many odd numbers are in a list.


def odd_numbers_in_list(list_of_ints):
    count = 0
    for num in list_of_ints:
        if num % 2 == 1:
            count += 1
    return count


def testEqual(a, b):
    """ Home-rolled test for equality """
    if a == b:
        print('Pass')
    else:
        print('Fail')


def main():
    """ Cursory test of odd_numbers_in_list(l) """

    testEqual(odd_numbers_in_list([0, 1, 2, 3, 4]), 2)
    testEqual(odd_numbers_in_list([0, 0, 0]), 0)
    testEqual(odd_numbers_in_list([1]), 1)
    testEqual(odd_numbers_in_list([3, 5, 7, 9, 11]), 5)


if __name__ == '__main__':
    main()
