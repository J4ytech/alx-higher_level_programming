#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # The '^' symbol finds elements present in only one of the sets
    # It excludes anything they have in common
    return set_1 ^ set_2