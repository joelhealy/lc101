def is_sorted(string):
    """
    Returns True if string is sorted from least to greatest
    False otherwise.
    """
    
    ret_value = True
    for i in range(1, len(string) - 1):
        ret_value = ret_value and (string[i-1:i] <= string[i:i+1])
    return ret_value


def main():
    """ Cursory test of is_sorted(string) """
    
    if is_sorted("ABC") == True:
        print("Pass")
    else:
        print("Fail")

    if is_sorted("aBc") == False:
        print("Pass")
    else:
        print("Fail")
    
    if is_sorted("dog") == False:
        print("Pass")
    else:
        print("Fail")
        

if __name__ == "__main__":
    main()
    
