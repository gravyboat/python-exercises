from nose.tools import *
from exercises import ex17


def test_palindrome_sentence_recognizer():
    '''
    Check a basic sentence works as a palindrome
    '''

    filtered_sentence = ex17.palindrome_sentence_recognizer('Rise to vote sir')
    assert_true(filtered_sentence)


def test_not_palindrome_sentence_recognizer():
    '''
    Check a basic sentence doesn't work as a palindrome
    '''

    filtered_sentence = ex17.palindrome_sentence_recognizer('Just a test')
    assert_false(filtered_sentence)

