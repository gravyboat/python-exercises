from nose.tools import *
from exercises import ex21


def test_char_freq():
    '''
    Check to make sure our translation is accurate
    '''

    test_char_freq_dict = ex21.char_freq('aaaabbbcc')
    assert_equal(test_char_freq_dict, {'a': 4, 'b': 3, 'c': 2})

