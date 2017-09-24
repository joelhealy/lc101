#  Write a function space_line(spaces, hashes) that returns a line with exactly
#  the specified number of spaces, followed by the specified number of hashes.
#
#  Example:
#
#      print(space_line(3,5))
#
#  Output:
#
#      #This is where the edge is, so there's 3 spaces before hashes
#         #####


def line(n, str):
    """Return a line consisting of <n> sequential copies of <str>)"""

    return_value = ''
    for _ in range(n):
        return_value += str
    return return_value


def space_line(spaces, hashes):
    """
    Return a line with exactly the specified number of spaces,
    followed by the specified number of hashes
    """

    return_value = line(spaces, ' ') + line(hashes, '#')
    return return_value


def main():
    """Run a quick check to validate space_line(spaces, hashes) function"""

    print('# <-- This is where the edge is')
    print('space_line(3, 5) -->')
    print(space_line(3, 5))


if __name__ == '__main__':
    main()
