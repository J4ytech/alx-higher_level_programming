#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    count = 0  # To track how many integers we actually print
    
    for i in range(x):
        try:
            # We try to print the element as an integer
            print("{:d}".format(my_list[i]), end="")
            count += 1  # Only increment if the print was successful
        except (ValueError, TypeError):
            # If it's a string/list, we catch the error and skip it
            pass
            
    # After the loop, print the trailing newline
    print("")
    
    return count
