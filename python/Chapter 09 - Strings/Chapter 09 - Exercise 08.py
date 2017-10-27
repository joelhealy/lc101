#  Write a function that decrypts the message from the previous exercise. It
#  should also take two parameters. The encrypted message, and the mixed up
#  alphabet. The function should return a string that is the same as the
#  original unencrypted message.


def decrypt_subst(encrypted_message, encrypted_alphabet):
    decrypted_message = ""
    for char in encrypted_message:
        if char in encrypted_alphabet:
            index = encrypted_alphabet.find(char)
            decrypted_message += chr(ord('A') + index)
    return decrypted_message


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
    """
    Cursory test of decrypt_subst(encrypted_message, encrypted_alphabet)
    """

    message = "NOWISTHETIMEFORALLGOODMENTOCOMETOTHEAIDOFTHEIRCOUNTRY"
    encrypted_alphabet = "KSDLWRNXGEPQZMJYVATFIUCOHB"
    testEqual(decrypt_subst(encrypt_subst(message, encrypted_alphabet),
                            encrypted_alphabet), message)


if __name__ == "__main__":
    main()
