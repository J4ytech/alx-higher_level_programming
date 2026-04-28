#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # This line does two things automatically:
    # 1. If 'key' exists, it changes its value to 'value'
    # 2. If 'key' does NOT exist, it creates it
    a_dictionary[key] = value
    
    # Return the updated dictionary
    return a_dictionary