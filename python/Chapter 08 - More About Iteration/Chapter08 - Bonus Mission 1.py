def print_mult_table(n):
    """ Print the multiplication table up to <n> x <n> """
    
    for i in range(n + 1):
        for j in range(n + 1):
            print(i * j, end=" ") 
        print("")
            
            
def main():
    """ Cursory test of print_mult_table(n) """
    
    print("Below is the multiplication table up to 3 x 3")
    print_mult_table(3)
    

if __name__ == "__main__":
    main()
    
