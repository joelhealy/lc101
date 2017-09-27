#  Write a function that mirrors its argument.  For example, mirror('good')
#  should return a string holding the value gooddoog.  (Hint: Make use of the
#  reverse function).


def mirror(text):
    """ Mirror text """
    return text + reverse(text)


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
    """ Cursory test of mirror(text) """
    testEqual(mirror('good'), 'gooddoog')
    testEqual(mirror('Python'), 'PythonnohtyP')
    testEqual(mirror(''), '')
    testEqual(mirror('a'), 'aa')


if __name__ == main():
    main()
