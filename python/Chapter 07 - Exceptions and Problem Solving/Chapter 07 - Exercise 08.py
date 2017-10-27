#  Write a function stairs(n) that prints the pattern shown below, with
#  height n. Again, utilize your line function to do this.
#
#  Example:
#      stairs(5))
#
#  Output:
#
#      #
#      ##
#      ###
#      ####
#      #####


def line(n):
    """Return a line consisting of <n> octothorpes (line(3) --> '###')"""

    return_value = ''
    for _ in range(n):
        return_value += '#'
    return return_value


def stairs(n):
    """Return a right isosceles triangle of width and height <n>"""

    my_EOL = '\n'
    return_value = ''
    for l in range(n):
        return_value += line(l + 1) + my_EOL
    return return_value


def main():
    """Run a quick check to validate stairs(n) function"""

    print('stairs(5) -->')
    print(stairs(5))


if __name__ == '__main__':
    main()
