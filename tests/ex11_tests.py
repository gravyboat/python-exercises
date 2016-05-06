from nose.tools import *
from exercises import ex11

def test_generate_n_chars():
    '''
    Confirm our string is the right length
    '''

    test_n_chars = ex11.generate_n_chars(4, 'a')
    assert_equal(test_n_chars, 'aaaa')

