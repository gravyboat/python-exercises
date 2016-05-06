from nose.tools import *
from exercises import ex7

def test_reverse():
    '''
    Test our string reversal
    '''

    test_string_reversal = ex7.reverse('test')
    assert_equal(test_string_reversal, 'tset')

