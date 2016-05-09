from nose.tools import *
from exercises import ex24


def test_make_3sg_form_ies():
    '''
    Try out a verb with a y that should end in ies
    '''

    third_person_form = ex24.make_3sg_form('try')
    assert_equal(third_person_form, 'tries')


def test_make_3sg_form_es():
    '''
    Try out a verb with 0, ch, sh, x, z that should end in es
    '''

    third_person_form = ex24.make_3sg_form('march')
    assert_equal(third_person_form, 'marches')


def test_make_3sg_form_s():
    '''
    Try out a verb that should end with an s
    '''

    third_person_form = ex24.make_3sg_form('stand')
    assert_equal(third_person_form, 'stands')
