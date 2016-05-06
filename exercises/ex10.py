#!/usr/bin/python

def overlapping(first_list, second_list):
    '''
    Takes two lists and checks if they have at least one number in common
    '''
    
    for item in first_list:
        if item in second_list:
            return(True)
    return(False)
