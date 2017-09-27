#  Write a funciton that recognizes palindromes.  (Hint: user your reverse
#  function to make this easy!).


def testEqual(a, b):
    """ Hand-rolled testEqual """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def reverse(text):
    """ Return a reversed version of text """
    ret_value = ""
    for i in range(len(text) - 1, -1, -1):
        ret_value += text[i]
    return ret_value


def is_palindrome(text):
    """ Is text a palindrome? """
    return (reverse(text) == text)


def main():
    """ Cursory test of is_palindrome(text) """
    testEqual(is_palindrome('abba'), True)
    testEqual(is_palindrome('abab'), False)
    testEqual(is_palindrome('straw warts'), True)
    testEqual(is_palindrome('a'), True)
    testEqual(is_palindrome(''), True)


if __name__ == main():
    main()
