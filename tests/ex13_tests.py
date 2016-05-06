from nose.tools import *
from exercises import ex13

def test_max_in_list():
    '''
    Confirm we are finding the largest number
    '''

    test_max_in_list = ex13.max_in_list([1, 2, 3, 4, 2, 6, 2])
    assert_equal(test_max_in_list, 6)

