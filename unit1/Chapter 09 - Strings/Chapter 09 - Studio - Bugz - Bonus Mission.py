#  Bonus Mission
#
#      Write a function called stretch that takes in a string and doubles each
#      of the letters contained in the string. For example,
#      stretch("chihuahua") would return “cchhiihhuuaahhuuaa”.
#
#      Add an optional parameter to your stretch function that indicates how
#      many times each letter should be duplicated. The default value for this
#      optional parameter should be 2. For example, stretch("chihuahua", 4)
#      would return "cccchhhhiiiihhhhuuuuaaaahhhhuuuuaaaa" but
#      stretch("chihuahua") should still return “cchhiihhuuaahhuuaa”, as
#      before.
#
#      Add an additional optional parameter to your stretch function that
#      contains a list of characters. This version of stretch will only
#      duplicate letters that are contained in the list. The default value
#      for this new parameter should be the list of lowercase characters.
#      For example, stretch("chihuahua", 3, "ha") would return
#      “chhhihhhuaaahhhuaaa”.


def stretch(s, n=2, chars_to_multiply=""):
    """
    Return the string <s> with each of the letters repeated <n> times
    if the letter occurs in <chars_to_multiply>.
    """

    s_multiple_chars = ""
    if len(chars_to_multiply) == 0:
        chars_to_multiply = s
    for char in (s):
        if char in chars_to_multiply:
            s_multiple_chars += char * n
        else:
            s_multiple_chars += char
    return s_multiple_chars


def testEqual(a, b):
    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of stretch(s) """

    testEqual(stretch("chihuahua"), "cchhiihhuuaahhuuaa")
    testEqual(stretch("chihuahua", 4), "cccchhhhiiiihhhhuuuuaaaahhhhuuuuaaaa")
    testEqual(stretch("chihuahua", 3, "ha"), "chhhihhhuaaahhhuaaa")


if __name__ == "__main__":
    main()
