#!/usr/bin/python


def palindrome_sentence_recognizer(sentence_to_check):
    '''
    Checks if a sentence is a palindrome
    '''

    stripped_sentence = (''.join(e for e in sentence_to_check if e.isalnum()))
    stripped_sentence = stripped_sentence.lower()

    if stripped_sentence == stripped_sentence[::-1]:
        return(True)
    else:
        return(False)

