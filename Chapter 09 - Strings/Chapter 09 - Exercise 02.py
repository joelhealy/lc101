#  Write a function that will return the number of digits in an integer

import string


def num_digits(n):
    """Return number of digits in an integer"""

    count = 0
    for char in str(n):
        if char in string.digits:
            count += 1
    return count


def main():
    """Cursory testing of num_digits"""

    print("num_digits(237) =", num_digits(237))
    print("num_digits(-4) =", num_digits(-4))
    print("num_digits(12493) =", num_digits(12493))
    print("num_digits(0) =", num_digits(0))


if __name__ == "__main__":
    main()
