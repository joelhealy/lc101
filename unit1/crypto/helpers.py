#  Part 3 of Crypto Large Assignment for LaunchCode 101
#
#
#  Refactoring Shared Code
#
#-----------------------------------------------------------------------------
#  alphabet_position
#
#  Open up your caesar.py file in Visual Studio Code. In that file, write a
#  function alphabet_position(letter), which receives a letter (that is, a
#  string with only one alphabetic character) and returns the 0-based
#  numerical position of that letter within the alphabet.
#
#  Here are some example input parameter values, with the corresponding
#  return values.
#
#  letter 	Return value
#     a 	0
#     A 	0
#     b 	1
#     y 	24
#     z 	25
#     Z 	25
#
#  Note:  The function should be case-insensitive.
#
#  Note:  You can assume that your input will definitely be a letter.  Don't
#  worry about what might happen if somebody tries to use your function with
#  an input parameter that is something other than a single letter, like
#  alphabet_position("grandpa22!")


def alphabet_position(letter):
    """ Return the 0-based numerical position of letter """

    return ord(letter.lower()) - ord('a')


#-----------------------------------------------------------------------------
#  rotate_character
#
#  Next, write another helper function rotate_character(char, rot) which
#  receives a character char (that is, a string of length 1), and an integer
#  rot. Your function should return a new string of length 1, the result of
#  rotating char by rot number of places to the right.
#
#  Here are some example input values, with the corresponding return values.
#
#  char 	rot 	Return value
#  ----     ----    ------------
#   a 	     13	          n
#   a 	     14	          o
#   a 	     0 	          a
#   c 	     26	          c
#   c 	     27	          d
#   A 	     13	          N
#   z 	     1 	          a
#   Z 	     2 	          B
#   z 	     37	          k
#   ! 	     37	          !
#   6 	     13	          6
#
#  Note:  The upper or lower case of the letter should be preserved. For
#  example, rotate_character("A", 13) results in "N", rather than "n"
#
#  Note:  For non-alphabetical characters, you should ignore the rot argument
#  and simply return char untouched. For example, see "!" and "6" in the
#  table above.


def rotate_character(char, rot):
    """
    Return the result of rotating <char> by <rot> number of places to the
    right.  For non-alphabetical characters, simply return char untouched.
    """

    if char in "abcdefghijklmnopqrstuvwxyz":
        return chr(ord('a') + (alphabet_position(char) + rot) % 26)
    elif char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return chr(ord('A') + (alphabet_position(char) + rot) % 26)
    else:
        return char


def my_test_equal(a, b):
    """ Home-rolled version of testEqual """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory testing of alphabet_position and rotate_character """
    
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


if __name__ == "__main__":
    main()

