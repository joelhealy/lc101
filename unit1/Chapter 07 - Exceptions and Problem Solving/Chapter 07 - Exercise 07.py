#  Write a function rectangle(width, height) that returns a rectangle of the
#  width and height given by the parameters. Again, utilize your line function
#  to do this.
#
#  Example:
#
#      print(rectangle(5, 3))
#
#  Output:
#
#      #####
#      #####
#      #####


def line(n):
    """Return a line consisting of <n> octothorpes (line(3) --> '###')"""

    return_value = ''
    for _ in range(n):
        return_value += '#'
    return return_value


def rectangle(width, height):
    """Return a rectangle of octothorpes of the given width and height"""

    my_EOL = '\n'
    return_value = ''
    for _ in range(height):
        return_value += line(width) + my_EOL
    return return_value


def main():
    """Run a quick check to validate rectangle(width, height) function"""

    print('rectangle(5, 3) -->')
    print(rectangle(5, 3))


if __name__ == '__main__':
    main()
