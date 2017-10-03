#  Write a function replace(s, old, new) that replaces all occurences of old
#  with new in a string s:
#
#  test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')
#
#  s = 'I love spom! Spom is my favorite food. Spom, spom, spom, yum!'
#  test(replace(s, 'om', 'am'),
#       'I love spam! Spam is my favorite food. Spam, spam, spam, yum!')
#
#  test(replace(s, 'o', 'a'),
#       'I lave spam! Spam is my favarite faad. Spam, spam, spam, yum!')
#
#  Hint: use the split and join methods.


def replace(s, old, new):
    """
    Return a version of string <s> with all <old> substrings replaced
    with <new>
    """

    new_s = ""
    i = 0
    l = len(old)
    while i < len(s):
        if s[i:min(i + l, len(s))] == old:
            new_s += new
            i += l
        else:
            new_s += s[i]
            i += 1
    print(new_s)
    return new_s


def test(a, b):
    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of replace(s, old, new) """

    test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')

    s = 'I love spom! Spom is my favorite food. Spom, spom, spom, yum!'
    test(replace(s, 'om', 'am'),
         'I love spam! Spam is my favorite food. Spam, spam, spam, yum!')

    test(replace(s, 'o', 'a'),
         'I lave spam! Spam is my favarite faad. Spam, spam, spam, yum!')


if __name__ == "__main__":
    main()
