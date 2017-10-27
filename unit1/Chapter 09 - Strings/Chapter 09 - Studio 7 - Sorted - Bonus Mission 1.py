def chars_after_first_comma(string):
    # This code is designed to throw an exception if a comma is not present
    return len(string) - string.index(',') - 1


def main():
    """ Cursory test of chars_after_first_comma """
  
    test_string_1 = "Before you go to bed, you need to brush your teeth."
    if chars_after_first_comma(test_string_1) == 30:
        print("Pass")
    else:
        print("Fail")
        
    test_string_2 = "Under the warm sun, the cat slept deeply."
    if chars_after_first_comma(test_string_2) == 22:
        print("Pass")
    else:
        print("Fail")
    

if __name__ == "__main__":
    main()
    
