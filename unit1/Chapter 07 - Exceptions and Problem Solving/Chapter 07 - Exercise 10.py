#  Write a function triangle(n) that returns an upright triangle of height n.
#
#  Example:
#      print(triangle(5))
#
#  Output:
#
#          #
#         ###
#        #####
#       #######
#      #########


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


def triangle(n):
    """Return an upright triangle of height <n>"""

    my_EOL = '\n'
    return_value = ''
    for line in range(n):
        return_value += space_line(n - line - 1, line * 2 + 1) + my_EOL
    return return_value


def main():
    """Run a quick check to validate triangle(n) function"""

    print('triangle(5) -->')
    print(triangle(5))


if __name__ == '__main__':
    main()
