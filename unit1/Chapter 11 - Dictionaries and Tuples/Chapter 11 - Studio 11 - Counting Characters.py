def character_counts(string):
    """
    Calculate the number of times each character occurs in a string and print
    these stats to the console.
    """

    char_count_dict = {}

    #  Traverse the string counting characters
    for char in string:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1

    #  Print the character counts
    for key in char_count_dict:
        print("{}: {}".format(key, char_count_dict[key]))

    return char_count_dict


def my_test_equal(a, b):
    """ Home-rolled version of testEqual(a, b) """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of character_counts(string) """

    input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " + \
            "Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at " + \
            "sagittis augue. Praesent quis rhoncus justo. Aliquam erat " + \
            "volutpat. Donec sit amet suscipit metus, non lobortis massa. " + \
            "Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget " + \
            "massa. Donec nec velit non ligula efficitur luctus."

    char_count_dict = character_counts(input)

    print("####  Testing character_counts -----------------------------------")
    my_test_equal(char_count_dict["A"], 1)
    my_test_equal(char_count_dict["h"], 1)
    my_test_equal(char_count_dict["u"], 28)
    my_test_equal(char_count_dict["b"], 3)
    my_test_equal(char_count_dict["v"], 4)
    my_test_equal(char_count_dict["x"], 1)
    my_test_equal(char_count_dict["l"], 17)
    my_test_equal(char_count_dict["r"], 9)
    my_test_equal(char_count_dict["o"], 15)
    my_test_equal(char_count_dict["j"], 1)
    my_test_equal(char_count_dict["q"], 3)
    my_test_equal(char_count_dict["P"], 1)
    my_test_equal(char_count_dict["t"], 29)
    my_test_equal(char_count_dict["U"], 1)
    my_test_equal(char_count_dict["V"], 1)
    my_test_equal(char_count_dict["m"], 11)
    my_test_equal(char_count_dict["N"], 1)
    my_test_equal(char_count_dict["g"], 7)
    my_test_equal(char_count_dict[" "], 50)
    my_test_equal(char_count_dict["n"], 14)
    my_test_equal(char_count_dict["d"], 4)
    my_test_equal(char_count_dict["D"], 2)
    my_test_equal(char_count_dict["e"], 26)
    my_test_equal(char_count_dict["p"], 7)
    my_test_equal(char_count_dict["f"], 2)
    my_test_equal(char_count_dict["i"], 27)
    my_test_equal(char_count_dict["s"], 29)
    my_test_equal(char_count_dict["L"], 1)
    my_test_equal(char_count_dict["c"], 17)
    my_test_equal(char_count_dict["a"], 22)
    my_test_equal(char_count_dict[","], 4)
    my_test_equal(char_count_dict["."], 8)


if __name__ == "__main__":
    main()
