from nose.tools import *
from exercises import ex8

def test_palindrome():
    '''
    Test whether our palindrome check returns True
    '''

    test_is_palindrome = ex8.is_palindrome('radar')
    assert_true(test_palindrome)

def test_not_palindrome():
    '''
    Test whether our palindrome check returns False
    '''

    test_is_not_palindrome = ex8.is_palindrome('test')
    assert_false(test_is_not_palindrome)

