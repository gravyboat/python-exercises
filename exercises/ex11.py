#!/usr/bin/python

def generate_n_chars(str_length, char_to_use):
    '''
    Returns a string str_length long made of up char_to_use
    '''

    final_string = ''
    for i in range(str_length):
        final_string += char_to_use
    return(final_string)
