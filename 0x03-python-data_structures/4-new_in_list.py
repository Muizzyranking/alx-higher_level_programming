#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specified position without modifying
    the original list"""
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
