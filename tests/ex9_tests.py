from nose.tools import *
from exercises import ex9

def test_is_member_number():
    '''
    Test whether number exists in a list of numbers
    '''

    test_is_member = ex9.is_member(1, [1, 2, 3])
    assert_true(test_is_member)


def test_is_char_number():
    '''
    Test whether char exist in a list of chars
    '''

    test_is_member = ex9.is_member('a', ['a', 'b', 'c'])
    assert_true(test_is_member)


def test_is_not_member_number():
    '''
    Test whether number does not in a list of numbers
    '''

    test_is_member = ex9.is_member(4, [1, 2, 3])
    assert_false(test_is_member)


def test_is_not_char_number():
    '''
    Test whether char does not exist in a list of chars
    '''

    test_is_member = ex9.is_member('d', ['a', 'b', 'c'])
    assert_false(test_is_member)

