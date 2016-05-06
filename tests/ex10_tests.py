from nose.tools import *
from exercises import ex10

def test_overlapping():
    '''
    Check that we return true when something overlaps
    '''

    test_overlapping_number = ex10.overlapping([1, 2, 3], [1, 3, 4])
    assert_true(test_overlapping_number)

def test_no_overlapping():
    '''
    Check that we return false when nothing overlaps
    '''

    test_overlapping_number = ex10.overlapping([1, 2, 3], [4, 5, 6])
    assert_false(test_overlapping_number)
