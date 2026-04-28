#!/usr/bin/python3

def uniq_add(my_list=[]):
    # set(my_list) removes all duplicate numbers
    # sum(...) adds whatever is inside the brackets
    return sum(set(my_list))