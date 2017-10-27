#  Here’s a table of English to Pirate translations:
#
#      English 	    Pirate
#      sir 	        matey
#      hotel 	    fleabag inn
#      student 	    swabbie
#      boy 	        matey
#      madam 	    proud beauty
#      professor 	foul blaggart
#      restaurant 	galley
#      your 	    yer
#      excuse 	    arr
#      students 	swabbies
#      are 	        be
#      lawyer 	    foul blaggart
#      restroom 	th’ head
#      my 	        me
#      hello 	    avast
#      is 	        be
#      man 	        matey
#
#  Write a program that asks the user for a sentence in English and then
#  translates that sentence to Pirate.


def translate(text):

    trans_dict = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "boy": "matey",
        "madam": "proud beauty",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "lawyer": "foul blaggart",
        "restroom": "head",
        "my": "me",
        "hello": "avast",
        "is": "be",
        "man": "matey",
        "the": "th'"}

    word_list = text.split()
    pirate_list = []
    for word in word_list:
        punctuation = ""
        if word[-1] in ",.;!?":
            punctuation = word[-1]
            word = word[:len(word) - 1]
        pirate_list.append(trans_dict.get(word, word) + punctuation)
    return " ".join(pirate_list)


def my_test_equal(a, b):
    """ Home-rolled version of testEqual() """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of translate(text) """
    text = "hello my man, please excuse your professor to the restroom!"
    my_test_equal(translate(text),
                  "avast me matey, please arr yer foul blaggart to th' head!")


if __name__ == "__main__":
    main()
