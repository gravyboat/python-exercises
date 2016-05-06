from nose.tools import *
from exercises import ex16


def test_filter_long_words():
    '''
    Ensure we are finding words that meet the minimum length
    '''

    filtered_words_list = ex16.filter_long_words(['test', 'test12'], 4)
    assert_equal(filtered_words_list, ['test12'])


def test_filter_long_words_empty():
    '''
    Ensure we return an empty list if nothing matches
    '''

    filtered_words_list = ex16.filter_long_words(['test', 'abcd'], 4)
    assert_equal(filtered_words_list, [])

