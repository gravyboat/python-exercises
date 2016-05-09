from nose.tools import *
from exercises import ex26


def test_max_in_list():
    '''
    Test out our max in list
    '''
    
    max_num_test = ex26.max_in_list([1, 2, 3])
    assert_equal(max_num_test, 3)

