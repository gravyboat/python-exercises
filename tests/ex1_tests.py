from nose.tools import *
from exercises import ex1

def test_max_val_first_larger():
    '''
    Test when our first value is larger
    '''

    test_max = ex1.max_val(2, 1)
    assert_equal(test_max, 2)


def test_max_val_second_larger():
    '''
    Test when our second value is larger
    '''

    test_max = ex1.max_val(1, 2)
    assert_equal(test_max, 2)
