#  Write a function diamond(n) that returns a diamond where the triangle
#  formed by the top portion has height n.  Notice that this means the
#  diamond has 2n - 1 rows.
#
#  Example:
#      print(diamond(5))
#
#  Output:
#
#          #
#         ###
#        #####
#       #######
#      #########
#       #######
#        #####
#         ###
#          #


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


def diamond(n):
    """
    Return a diamond where the triangle formed by the top portion
    has height n.
    """

    my_EOL = '\n'
    return_value = ''
    for line in range(n):
        return_value += space_line(n - line - 1, line * 2 + 1) + my_EOL
    for line in range(n - 1):
        return_value += space_line(line + 1, 2 * (n - line) - 3) + my_EOL
    return return_value


def main():
    """Run a quick check to validate diamond(n) function"""

    print('diamond(5) -->')
    print(diamond(5))


if __name__ == '__main__':
    main()
