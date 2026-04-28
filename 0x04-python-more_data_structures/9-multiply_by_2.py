#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # 1. Create a brand new empty dictionary
    new_dict = {}
    
    # 2. Loop through all the keys in the original dictionary
    for key in a_dictionary:
        # 3. Get the old value, multiply it by 2
        value = a_dictionary[key]
        new_value = value * 2
        
        # 4. Save this into the new dictionary with the same key
        new_dict[key] = new_value
        
    # 5. Return the finished new dictionary
    return new_dict