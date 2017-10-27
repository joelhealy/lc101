#  Write a function that removes the first occurrence of a string from
#  another string.


def remove(substr, original_string):
    if substr in original_string:
        i_start = original_string.find(substr)
        i_end = i_start + len(substr)
        ret_value = original_string[:i_start] + original_string[i_end:]
    else:
        ret_value = original_string
    return ret_value


def testEqual(a, b):
    """ Hand-rolled testEqual """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of remove(substr, original-string) """
    testEqual(remove('an', 'banana'), 'bana')
    testEqual(remove('cyc', 'bicycle'), 'bile')
    testEqual(remove('iss', 'Mississippi'), 'Missippi')
    testEqual(remove('egg', 'bicycle'), 'bicycle')
    testEqual(remove('oo', 'Yahoohoo'), 'Yahhoo')


if __name__ == "__main__":
    main()
