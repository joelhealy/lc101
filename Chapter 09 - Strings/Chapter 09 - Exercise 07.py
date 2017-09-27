#  Write a function that implements a substitution cipher. In a substitution
#  cipher one letter is substituted for another to garble the message. For
#  example A -> Q, B -> T, C -> G etc. your function should take two
#  parameters, the message you want to encrypt, and a string that represents
#  the mapping of the 26 letters in the alphabet. Your function should return
#  a string that is the encrypted version of the message.


def encrypt_subst(message, encrypted_alphabet):
    encrypted_message = ""
    for i in range(len(message)):
        alpha_index = ord(message[i]) - ord('A')
        encrypted_message += encrypted_alphabet[alpha_index]
    return encrypted_message


def testEqual(a, b):
    """ Hand-rolled testEqual """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of encrypt_subst(message, encrypted_alphabet) """

    encrypted_alphabet = "KSDLWRNXGEPQZMJYVATFIUCOHB"
    testEqual(encrypt_subst("ABCDEFGHIJKLMNOPQRSTUVWXYZ", encrypted_alphabet),
              encrypted_alphabet)


if __name__ == "__main__":
    main()
