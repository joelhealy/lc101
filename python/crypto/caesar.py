#-----------------------------------------------------------------------------
#  Part 1 of Crypto Large Assignment for LaunchCode 101
#
#  (including Bonus Missions 1 & 2 and Bonus Bonus Mission)


from helpers import alphabet_position, rotate_character


#-----------------------------------------------------------------------------
#  encrypt
#
#  Now let's get to the heart of the matter.  Write one more function called
#  encrypt(text, rot), which receives as input a string and an integer. This
#  is just like the rot13 function, but instead of hardcoding the number 13,
#  your function should receive a second argument, rot which specifies the
#  rotation amount. Your function should return the result of rotating each
#  letter in the text by rot places to the right.
#
#  Here are some example input values, with the corresponding return values:
#
#  text 	        rot 	Return value
#  -------------    ----    -------------
#  a 	            13 	    n
#  abcd 	        13 	    nopq
#  LaunchCode 	    13 	    YnhapuPbqr
#  LaunchCode 	    1 	    MbvodiDpef
#  Hello, World! 	5 	    Mjqqt, Btwqi!
#
#  Note:  The text argument might contain non-alphabetic characters (spaces,
#  numbers, symbols). You should leave these as they are.


def encrypt(text, rot):
    """
    Return encrpted <text> resulting from rotating each character by <rot>
    places to the right
    """

    encrypted_text = ""
    for char in text:
        encrypted_text += rotate_character(char, rot)
    return encrypted_text


#  Make It Interactive
#
#  You're almost done with Caesar!  The last step is simply to write some
#  print and input statements so the user can run your program from the
#  terminal.  Remember, you should ask the user for their message and
#  rotation amount, and then print the encrypted message:
#
#      $ python caesar.py
#      Type a message:
#      Hello, World!
#      Rotate by:
#      5
#      Mjqqt, Btwqi!


def main():
    from sys import argv, exit

    #  Print usage and exit if no arguments are given
    if len(argv) < 2:
        print("usage: python {0} n".format(argv[0]))
        exit()

    #  Print usage and exit if first argument is not an integer
    rot = argv[1]
    if not rot.isdigit():
        print("usage: python {0} n".format(argv[0]))
        print()
        print("   Arguments:")
        print()
        print("      -n : The number of characters to rotate when encrypting")
        print("           the message.  Must be an integer.")
        exit()

    msg = input("Type a message:\n")
    print(encrypt(msg, int(rot)))


def my_test_equal(a, b):
    """ Home-rolled version of testEqual """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def my_test():
    """ Cursory testing of caesar.py functions """
    
    #  alphabet_position(letter) 

    print("Testing alphabet_position(letter)...\n")
    my_test_equal(alphabet_position('a'), 0)
    my_test_equal(alphabet_position('A'), 0)
    my_test_equal(alphabet_position('b'), 1)
    my_test_equal(alphabet_position('y'), 24)
    my_test_equal(alphabet_position('z'), 25)
    my_test_equal(alphabet_position('Z'), 25)
    print()

    #  rotate_character(char, rot)

    print("Testing rotate_character(char, rot)...\n")
    my_test_equal(rotate_character('a', 13), 'n')
    my_test_equal(rotate_character('a', 14), 'o')
    my_test_equal(rotate_character('a', 0), 'a')
    my_test_equal(rotate_character('c', 26), 'c')
    my_test_equal(rotate_character('c', 27), 'd')
    my_test_equal(rotate_character('A', 13), 'N')
    my_test_equal(rotate_character('z', 1), 'a')
    my_test_equal(rotate_character('Z', 2), 'B')
    my_test_equal(rotate_character('z', 37), 'k')
    my_test_equal(rotate_character('!', 37), '!')
    my_test_equal(rotate_character('6', 13), '6')
    print()


    #  encrypt(text, rot)

    print("Testing encrypt(text, rot)...\n")
    my_test_equal(encrypt('a', 13), 'n')
    my_test_equal(encrypt('abcd', 13), 'nopq')
    my_test_equal(encrypt('LaunchCode', 13), 'YnhapuPbqr')
    my_test_equal(encrypt('LaunchCode', 1), 'MbvodiDpef')
    my_test_equal(encrypt('Hello, World!', 5), 'Mjqqt, Btwqi!')
    print()


if __name__ == "__main__":
    # my_test()
    main()

