from nose.tools import *
from exercises import ex23


def test_correct_duplicate_spaces():
    '''
    Make sure we remove duplicate spaces
    '''

    correct_duplicate_spaces = ex23.correct('A   test')
    assert_equal(correct_duplicate_spaces, 'A test')


def test_correct_space_after_punctuation():
    '''
    Make sure we add a space after a period if needed
    '''

    correct_space_punctuation = ex23.correct('A test.Thing')
    assert_equal(correct_space_punctuation, 'A test. Thing')

def test_correct_punctuation_and_duplicate():
    '''
    Make sure we add a space after a period if needed, and remove spaces
    '''

    correct_both = ex23.correct('A   test.Thing')
    assert_equal(correct_both, 'A test. Thing')
