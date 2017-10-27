#  Write a function line(n) that returns a line with exactly n hashes.
#
#  Example:
#
#      print(line(5))
#  Output:
#
#      #####


def line(n):
    """Return a line consisting of <n> octothorpes (line(3) --> '###')"""

    return_value = ''
    for _ in range(n):
        return_value += '#'
    return return_value


def main():
    """Run a quick check to validate line(n) function"""

    print('line(5) --> ' + line(5))


if __name__ == '__main__':
    main()
