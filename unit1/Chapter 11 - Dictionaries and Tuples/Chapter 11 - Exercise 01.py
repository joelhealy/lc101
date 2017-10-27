#  Write a program that allows the user to enter a string. It then prints a
#  table of the letters of the alphabet in alphabetical order which occur in
#  the string together with the number of times each letter occurs. Case
#  should be ignored. A sample run of the program might look like this:
#
#  Please enter a sentence: ThiS is a String with Upper and lower case Letters.
#      a  3
#      c  1
#      d  1
#      e  5
#      g  1
#      h  2
#      i  4
#      l  2
#      n  2
#      o  1
#      p  2
#      r  4
#      s  5
#      t  5
#      u  1
#      w  2
#  $


def print_dict_sorted(dict):
    """
    Print the individual items in dictionary <dict> one per line sorted by key.
    Each line should contain a key followed by two spaces followed by the
    associated value.
    """

    lst = list(dict.keys())
    lst.sort()
    for key in lst:
        print("{0}  {1}".format(key, dict[key]))


def string_to_letter_counts(str):
    """
    Given an input string <str>, return a dictionary whose keys are the letters
    of the alphabet which occur in the string and whose values are the number
    of times each letter occurs.  Case should be ignored.
    """

    dict = {}
    for char in str:
        if char.isalpha():
            char = char.lower()
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

    return dict


def testEqual(a, b):
    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of string_to_letter_counts(str) """

    testEqual(string_to_letter_counts("xyz"), {'x': 1, 'y': 1, 'z': 1})
    testEqual(string_to_letter_counts("Zyx"), {'x': 1, 'y': 1, 'z': 1})

    print_dict_sorted(string_to_letter_counts(
        "ThiS is a String with Upper and lower case Letters."))


if __name__ == "__main__":
    main()
