#  Count how many words in a list have length 5.


def how_many_fives(words):
    """ Count how many words in a list have length 5 """

    count = 0
    for word in words:
        if len(word) == 5:
            count += 1
    return count


def testEqual(a, b):
    """ Home-rolled testEqual """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of how_many_fives(words) """

    testEqual(how_many_fives(["", "", "", "", ""]), 0)
    testEqual(how_many_fives(["fiver", "four", "six", "twerk", ""]), 2)
    testEqual(how_many_fives(["abcde", "abcdef", "wrstik", "length", "six"]), 1)
    testEqual(how_many_fives(["abcde", "fghij", "klmno"]), 3)


if __name__ == "__main__":
    main()
