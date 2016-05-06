#!/usr/bin/python


def find_longest_word(list_of_words):
    '''
    Takes a list of words and returns the length of the longest one
    '''

    longest_word_length = 0

    for word in list_of_words:
        if len(word) > longest_word_length:
            longest_word_length = len(word)
    return(longest_word_length)
