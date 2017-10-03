#  Although Python provides us with many list methods, it is good practice and
#  very instructive to think about how they are implemented. Implement your own
#  Python functions that works like the following built-in ones:
#
#    a. count
#    b. in
#    c. reverse
#    d. index
#    e. insert
#
#  Note that you cannot call your version of the in function “in”, since that
#  is a reserved keyword.  You could call it is_in instead.


def count(val, list):
    """ Count the number of items which are <val> in the <list> """

    total = 0
    for item in list:
        if item == val:
            total += 1
    return total


def is_in(val, list):
    """ Is <val> in the <list> """

    found = False
    for item in list:
        if item == val:
            found = True
    return found


def reverse(list):
    """ Return a reversed version of <list> """

    reversed = []
    for index in range(len(list) - 1, -1, -1):
        reversed += [list[index]]
    return reversed


def index(val, list):
    """ Return the index of the leftmost item in list which is <val> """

    found_index = -1
    for i in range(len(list)):
        if list[i] == val:
            found_index = i
            break

    return found_index


def insert(item, index, list):
    """ Insert <item> into <list> at position <index> """

    new_list = []
    for i in range(len(list)):
        if i == index:
            new_list.append(item)
        new_list.append(list[i])
    if index == len(list):
        new_list.append(item)

    return new_list


def testEqual(a, b):
    """ Home-rolled testEqual """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of how_many_fives(words) """

    print("Testing count -------------------------------------------")
    testEqual(count("abc", ["abc", "defg", "abcd", "abc", "r"]), 2)
    testEqual(count("abc", ["abr", "defg", "abcd", "bbc", "r"]), 0)
    testEqual(count("abc", ["abc", "abc", "abcd", "abc", "d"]), 3)

    print("Testing is_in -------------------------------------------")
    testEqual(is_in("abc", ["abc", "defg", "abcd", "abc", "r"]), True)
    testEqual(is_in("abc", ["abr", "defg", "abcd", "bbc", "r"]), False)
    testEqual(is_in("abc", ["abc"]), True)

    print("Testing reverse -------------------------------------------")
    testEqual(reverse(["abc"]), ["abc"])
    testEqual(reverse([1, 2, 3, 4]), [4, 3, 2, 1])
    testEqual(reverse([]), [])

    print("Testing index -------------------------------------------")
    testEqual(index("abc", ["abc", "defg", "abcd", "abc", "r"]), 0)
    testEqual(index("abc", ["abr", "defg", "abcd", "bbc", "r"]), -1)
    testEqual(index("abc", ["def", "xyz", "abcd", "abc", "d"]), 3)

    print("Testing insert -------------------------------------------")
    testEqual(insert("abc", 0, ["def", "xyz", "p", "qrs", "d"]),
              ["abc", "def", "xyz", "p", "qrs", "d"])
    testEqual(insert("abc", 2, ["def", "xyz", "p", "qrs", "d"]),
              ["def", "xyz", "abc", "p", "qrs", "d"])
    testEqual(insert("abc", 5, ["def", "xyz", "p", "qrs", "d"]),
              ["def", "xyz", "p", "qrs", "d", "abc"])


if __name__ == "__main__":
    main()
