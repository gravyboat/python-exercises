#!/usr/bin/python


def make_ing_form(verb_to_make_present):
    '''
    Takes a word's infinitive form and makes it present, rate -> rating
    Note that this doesn't cover all exceptions
    '''

    if verb_to_make_present.endswith('ie'):
        present_form = verb_to_make_present[:-2] + 'ying'
    elif verb_to_make_present.endswith('e') and not verb_to_make_present.endswith('ee'):
        present_form = verb_to_make_present[:-1] + 'ing'
    else:
        present_form = verb_to_make_present + 's'

    return(present_form)

