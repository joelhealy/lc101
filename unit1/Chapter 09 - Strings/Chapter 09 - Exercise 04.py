#  Write a function reverse that receives a string argument, and returns a
#  reversed version of the string


def reverse(text):
    """ Return a reversed version of text """
    ret_value = ""
    for i in range(len(text) - 1, -1, -1):
        ret_value += text[i]
    return ret_value


def testEqual(a, b):
    """ Hand-rolled testEqual """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of reverse(text) """

    testEqual(reverse("happy"), "yppah")
    testEqual(reverse("Python"), "nohtyP")
    testEqual(reverse(""), "")


if __name__ == "__main__":
    main()
