from nose.tools import *
from exercises import ex2

def test_max_of_three_first_largest():
    '''
    Test when our first value is largest
    '''

    test_max = ex2.max_of_three(3, 2, 1)
    assert_equal(test_max, 3)


def test_max_of_three_second_largest():
    '''
    Test when our second value is largest
    '''

    test_max = ex2.max_of_three(2, 3, 1)
    assert_equal(test_max, 3)


def test_max_of_three_third_largest():
    '''
    Test when our third value is largest
    '''

    test_max = ex2.max_of_three(1, 2, 3)
    assert_equal(test_max, 3)
