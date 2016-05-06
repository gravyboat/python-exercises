#!/usr/bin/python

def is_palindrome(word_to_check):
    '''
    Checks if a word is a palindrome
    '''

    if word_to_check == word_to_check[::-1]:
        return(True)
    else:
        return(False)
