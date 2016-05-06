#!/usr/bin/python

def is_member(item_to_check, list_to_check):
    '''
    Checks if an item is in a list
    '''

    for list_item in list_to_check:
        if item_to_check == list_item:
            return(True)

    return(False)

