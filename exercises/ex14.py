#!/usr/bin/python


def map_words_to_integers(list_of_words):
    '''
    Maps a list of words to their length as an int
    '''

    length_of_words = [len(elem) for elem in list_of_words]
    return(length_of_words)

