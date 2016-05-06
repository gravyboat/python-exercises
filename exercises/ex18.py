#!/usr/bin/python


def check_if_pangram(string_to_check):
    '''
    Check if a string is a pangram (uses all letters of alphabet)
    '''

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in alphabet:
        if char not in string_to_check:
            return(False)
    
    return(True)

