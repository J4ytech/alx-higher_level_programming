#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # 1. Create a brand new empty list to hold our results
    new_list = []
    
    # 2. Look at every element in the original list one by one
    for element in my_list:
        # 3. Check: is this the element we want to swap?
        if element == search:
            # If yes, add the 'replace' value to our new list
            new_list.append(replace)
        else:
            # If no, add the original element to our new list
            new_list.append(element)
            
    # 4. Give back the finished new list
    return new_list