def power(x, n):
    """Calculate x to the exponent n"""

    running_product = 1
    for counter in range(n):
        running_product *= x

    return running_product


def main():
    num = 10
    p = 4
    result = power(num, p)
    print("The result of", num, "to the power", p, "is", result)


if __name__ == '__main__':
    main()
