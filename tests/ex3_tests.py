from nose.tools import *
from exercises import ex3

def test_max_val_first_larger():
    '''
    Test if our string is returning the proper length
    '''

    test_string_length = ex3.str_length('test')
    assert_equal(test_string_length, 4)


