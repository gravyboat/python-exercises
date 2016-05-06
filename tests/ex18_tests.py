from nose.tools import *
from exercises import ex18


def test_check_if_pangram():
    '''
    Check if string is a pangram
    '''

    is_pangram = ex18.check_if_pangram('abcdefghijklmnopqrstuvwxyz')
    assert_true(is_pangram)


def test_check_if_not_pangram():
    '''
    Check if string is not a pangram
    '''

    is_pangram = ex18.check_if_pangram('zzzghyujkiolp')
    assert_false(is_pangram)
