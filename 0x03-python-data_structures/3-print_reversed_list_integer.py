#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for nums in reversed(my_list):
            print("{}".format(nums))
