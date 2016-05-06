from nose.tools import *
from exercises import ex19
import sys
try:
    from StringIO import StringIO
except:
    from io import StringIO

def test_bottles_of_beer():
    '''
    Test our bottles_of_beer count
    '''

    std_out = sys.stdout
    result = StringIO()
    sys.stdout = result

    test_bottles = ex19.bottles_of_beer(1)
    sys.stdout = std_out

    result_string = result.getvalue()

    assert_equal(result_string,
                '1 bottles of beer on the wall, 1 bottles of beer.\nTake one down, pass it around, 0 bottles of beer on the wall.\n')

