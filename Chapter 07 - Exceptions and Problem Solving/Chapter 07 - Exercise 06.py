#  Write a function square(n) that returns an n by n square of hashes. Utilize
#  your line function.
#
#  Example:
#
#      print(square(5))
#
#  Output:
#
#      #####
#      #####
#      #####
#      #####
#      #####


def line(n):
    """Return a line consisting of <n> octothorpes (line(3) --> '###')"""

    return_value = ''
    for _ in range(n):
        return_value += '#'
    return return_value


def square(n):
    """Return an <n> x <n> square of octothorpes"""

    my_CRLF = '\n'
    return_value = ''
    for _ in range(n):
        return_value += line(n) + my_CRLF
    return return_value


def main():
    """Run a quick check to validate square(n) function"""

    print('square(5) -->')
    print(square(5))


if __name__ == '__main__':
    main()
