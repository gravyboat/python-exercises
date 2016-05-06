from nose.tools import *
from exercises import ex5

def test_translate():
    '''
    Test out our translation method
    '''

    test_translation = ex5.translate('test')
    assert_equal(test_translation, 'totesostot')

