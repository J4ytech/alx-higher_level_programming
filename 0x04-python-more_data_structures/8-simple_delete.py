#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # 1. Check if the key actually exists in the dictionary
    if key in a_dictionary:
        # 2. If it exists, delete it
        del a_dictionary[key]
    
    # 3. Return the dictionary (modified or not)
    return a_dictionary