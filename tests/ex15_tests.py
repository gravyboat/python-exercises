from nose.tools import *
from exercises import ex15


def test_find_longest_word():
    '''
    Confirm we are getting the proper word length
    '''

    longest_word = ex15.find_longest_word(['test', 'test2', 'test12'])
    assert_equal(longest_word, 6)

