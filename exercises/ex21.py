#!/usr/bin/python


def char_freq(string_to_count):
    '''
    Count the frequency of each character in a string
    '''

    char_frequency_dict = {}

    for char in string_to_count:
        if char not in char_frequency_dict:
            char_frequency_dict[char] = 1
        else:
            char_frequency_dict[char] += 1
    
    return(char_frequency_dict)

