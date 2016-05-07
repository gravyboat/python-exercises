from nose.tools import *
from exercises import ex20


def test_translate():
    '''
    Check to make sure our translation is accurate
    '''

    test_translation = ex20.translate(['merry', 'happy', 'new'])
    assert_equal(test_translation, ['god', 'gott', 'nytt'])


def test_empty_translate():
    '''
    Check to see that we return an empty list when it does not match
    '''

    test_translation = ex20.translate(['ask', 'test', 'blarg'])
    assert_equal(test_translation, [])
