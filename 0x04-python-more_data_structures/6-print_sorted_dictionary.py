#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # 1. Get all the keys and sort them alphabetically
    sorted_keys = sorted(a_dictionary.keys())
    
    # 2. Loop through the sorted list of keys
    for key in sorted_keys:
        # 3. Print the key and its corresponding value
        # Use .format() or f-strings to match the required output style
        print("{}: {}".format(key, a_dictionary[key]))