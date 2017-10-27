def fib(n):
    """Calculate the nth Fibonacci number"""

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # return fib(n - 1) + fib(n - 2)
        # using the recursive algorithm above is too time-consuming
        # the iterative approach below works better
        penult = 0
        ult = 1
        for i in range(1, n):
            fib_calc = penult + ult
            penult = ult
            ult = fib_calc
        return fib_calc


def main():
    for n in range(250):
        print("fib(" + str(n) + ") =", fib(n))


if __name__ == '__main__':
    main()
