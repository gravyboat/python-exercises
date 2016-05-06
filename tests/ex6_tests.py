from nose.tools import *
from exercises import ex6

def test_sum():
    '''
    Test out if our sum is correct
    '''

    test_sum_total = ex6.sum(1, 2,3 ,4)
    assert_equal(test_sum_total, 10)

def test_multiply():
    '''
    Test out if multiplication works
    '''

    test_multiply_total = ex6.multiply(1, 2, 3, 4)
    assert_equal(test_multiply_total, 24)

