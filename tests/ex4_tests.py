from nose.tools import *
from exercises import ex4

def test_is_vowel():
    '''
    Test whether a letter is a vowel
    '''

    test_vowel = ex4.is_vowel('a')
    assert_true(test_vowel)

def test_is_not_vowel():
    '''
    Test whether a letter is not a vowel
    '''
    
    test_vowel = ex4.is_vowel('z')
    assert_false(test_vowel)
