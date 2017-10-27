def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """

    initials = ""
    ready_for_init = True
    for char in fullname:
        if char.isspace():
            ready_for_init = True
        elif ready_for_init:
            initials += char.upper()
            ready_for_init = False

    return initials


def main():
    """ Cursory test of get_initials(fullname) """

    # print("The initials of 'Ozzie Smith' are", get_initials("Ozzie Smith"))
    # print("The initials of 'Bonnie blair' are", get_initials("Bonnie blair"))
    # print("The initials of 'George' are", get_initials("George"))
    # print("The initials of 'Daniel Day Lewis' are", get_initials("Daniel Day Lewis"))

    name = input("What is your full name?\n")
    print(get_initials(name))


if __name__ == '__main__':
    main()

