from nose.tools import *
from exercises import ex25


def test_make_ing_form_ie():
    '''
    Test for ie match
    '''

    present_verb = ex25.make_ing_form('tie')
    assert_equal(third_person_form, 'tying')


def test_make_ing_form_e():
    '''
    Test for e match
    '''

    present_verb = ex25.make_ing_form('grate')
    assert_equal(third_person_form, 'grating')


def test_make_ing_form_s():
    '''
    Test for other matches
    '''

    present_verb = ex25.make_ing_form('grab')
    assert_equal(third_person_form, 'grabs')
