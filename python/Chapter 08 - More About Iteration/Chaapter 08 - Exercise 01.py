#  Write a function print_triangular_numbers(n) that prints out the first n
#  triangular numbers. A call to print_triangular_numbers(5) would produce
#  the following output:
#
#      1
#      3
#      6
#      10
#      15


def print_triangular_numbers(n):
    """Print out the first <n> triangular numbers"""

    sum = 0
    for i in range(1, n + 1):
        sum += i
        print(sum)


def main():
    """Perform a cursory test to validate print_triangular_numbers(n)"""

    print("The first 5 trianglular numbers are:")
    print_triangular_numbers(5)


if __name__ == '__main__':
    main()
