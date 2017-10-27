def move_consonants_to_end(string):
    consonants = 'bcdfghjklmnpqrstvwxz'
    init_consonants = ''
    for char in string:
        if char in consonants:
            init_consonants += char
        else:
            break
    return string[len(init_consonants):] + init_consonants


def pig_latinize(string):
    ret_value = ""
    for word in string.split():
        ret_value += move_consonants_to_end(word) + "ay "
    return ret_value.rstrip()


def main():
    """ Cursory test of pig_latinize(string) """
    
    mystring = "python code wins"
    if pig_latinize(mystring) == "ythonpay odecay insway":
        print("Pass")
    else:
        print("Fail - " + pig_latinize(mystring))
        
    mystring = "all open androids"
    if pig_latinize(mystring) == "allay openay androidsay":
        print("Pass")
    else:
        print("Fail - " + pig_latinize(mystring))
        
        
if __name__ == "__main__":
    main()
    

