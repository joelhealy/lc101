#  Write a function called rot13 that uses the Caesar cipher to encrypt a
#  message. The Caesar cipher works like a substitution cipher but each
#  character is replaced by the character 13 characters to “its right” in the
#  alphabet. So for example the letter “a” becomes the letter “n”. If a letter
#  is past the middle of the alphabet then the counting wraps around to the
#  letter “a” again, so “n” becomes “a”, “o” becomes “b” and so on. Hint:
#  Whenever you talk about things wrapping around its a good idea to think of
#  modulo arithmetic (using the remainder operator).

import string


def rot13(mess):
    """ Encrypt <mess> using the Caesar cipher """

    encrypted_message = ""
    for char in mess:
        if char in string.ascii_lowercase:
            index = (ord(char) - ord('a') + 13) % 26
            encrypted_message += chr(ord('a') + index)
        else:
            encrypted_message += char
    return encrypted_message


def main():
    print(rot13('abcde'))
    print(rot13('nopqr'))
    print(rot13(rot13(
        'since rot thirteen is symmetric you should see this message')))


if __name__ == "__main__":
    main()
