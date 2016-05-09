#!/usr/bin/python


import re


def correct(string_to_correct):
    '''
    Make sure our grammar is correct related to spaces
    This includes no double spaces and a space after punctuation
    '''

    removed_duplicate_spaces = re.sub(' +', ' ', string_to_correct)

    space_after_period = re.sub(r'\.([a-zA-Z])', r'. \1', removed_duplicate_spaces)

    return(space_after_period)
