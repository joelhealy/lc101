#-----------------------------------------------------------------------------
#  Part 2 of Crypto Large Assignment for LaunchCode 101
#
#  (including Bonus Missions 1 & 2 and Bonus Bonus Mission)
#
#
#  Your finished program will behave like this:
#
#      $ python vigenere.py
#      Type a message:
#      The crow flies at midnight!
#      Encryption key:
#      boom
#      Uvs osck rmwse bh auebwsih!
#
#  Above, the user entered a message of "The crow flies at midnight!" and
#  an encryption key of "boom", and the program printed
#  "Uvs osck rmwse bh auebwsih!".
#
#  How did we arrive at that result? Here is a detailed breakdown:
#
#  char from input string 	char from key 	rotation amount 	result char
#  ----------------------   -------------   ---------------     -----------
#             T 	              b 	           1 	             U
#             h 	              o 	           14 	             v
#             e 	              o 	           14 	             s
#          (space) 	             n/a 	          n/a 	          (space)
#             c 	              m 	           12 	             o
#             r 	              b 	           1 	             s
#             o 	              o 	           14 	             c
#             w 	              o 	           14 	             k
#          (and so on ...) 	  	  	 
#
#  Note:  As with Caesar, the upper or lower case of each character should
#  be preserved, and non-alphabetical characters like " " and "!" should not
#  get encrypted.
#
#  Note:  When we encounter a non-alphabetical character in the message,
#  the encryption key does not use up another letter. For example, notice
#  how the "m" in "boom" does not get "wasted", so to speak, on the space
#  character. Instead, it is "saved" for the next alphabetical character,
#  the "c" in "crow".
#
#  Note:  Whenever we reach the end of the encryption key ("boom") before
#  reaching the end of the message, the encryption key wraps back around
#  to the beginning again (the letter "b").
#
#  Note:  You may assume that the encryption key ("boom") will not contain
#  any numbers or special characters. Letters only.


from helpers import alphabet_position, rotate_character


#-----------------------------------------------------------------------------
#  encrypt
#
#  Now go ahead and write a new version of the encrypt function which uses
#  the Vigenere cipher rather than Caesar.


def encrypt(text, key):
    """
    Return <text> encrypted with a Vigenere cipher using <key>
    """

    rotation_list = []
    for char in key:
        rotation_list.append(alphabet_position(char))

    rl_index = 0
    encrypted_text = ""
    for char in text:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            encrypted_text += rotate_character(char, rotation_list[rl_index])
            rl_index = (rl_index + 1) % len(key)
        else:
            encrypted_text += char
    return encrypted_text


#  Make It Interactive
#
#  Finally, add the appropriate print and input statements inside a main
#  function so that your program behaves as specified:
#
#      $ python vigenere.py
#      Type a message:
#      The crow flies at midnight!
#      Encryption key:
#      boom
#      Uvs osck rmwse bh auebwsih!


def main():
    from sys import argv, exit

    #  Print usage and exit if no keyword argument present
    if len(argv) < 2:
        print("usage: python {0} keyword".format(argv[0]))
        exit()

    #  Print usage and exit if keyword contains non-letters
    key = argv[1]
    if not key.isalpha():
        print("usage: python {0} keyword".format(argv[0]))
        print()
        print("   Arguments:")
        print()
        print('      -keyword : The sring to be used as a "key" to encrypt your message.')
        print("                 Should only contain alphabetic characters --")
        print("                 no numbers or special characters")
        exit()

    msg = input("Type a message:\n")
    print(encrypt(msg, key))


if __name__ == "__main__":
    main()

