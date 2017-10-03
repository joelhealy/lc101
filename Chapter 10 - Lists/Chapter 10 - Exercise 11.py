#  Write a function that will sum up all the elements in a list up to but not
#  including the first even number.


def sum_of_initial_odds(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
            break
        else:
            total += num
    return total


def testEqual(a, b):
    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of sum_of_initial_ods(nums) """

    testEqual(sum_of_initial_odds([1, 3, 1, 4, 3, 8]), 5)
    testEqual(sum_of_initial_odds([6, 1, 3, 5, 7]), 0)
    testEqual(sum_of_initial_odds([1, -7, 10, 23]), -6)
    testEqual(sum_of_initial_odds(range(1, 555, 2)), 76729)


if __name__ == "__main__":
    main()
