from nose.tools import *
from exercises import ex14


def test_map_words_to_integers():
    '''
    Confirm we are counting our length correctly
    '''

    mapped_word_length = ex14.map_words_to_integers(['test', 'test2'])
    assert_equal(mapped_word_length, [4, 5])

