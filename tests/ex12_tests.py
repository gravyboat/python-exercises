from nose.tools import *
from exercises import ex12
from io import StringIO
import sys

def test_histogram():
    '''
    Test our histogram output is correct
    '''

    std_out = sys.stdout
    result = StringIO()
    sys.stdout = result

    test_histogram = ex12.histogram([1, 2, 3])
    sys.stdout = std_out

    result_string = result.getvalue()

    assert_equal(result_string, '*\n**\n***\n')

