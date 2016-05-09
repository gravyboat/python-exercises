#!/usr/bin/python


def make_3sg_form(verb_to_third_person):
    '''
    Takes a word and makes it third person, for example try becomes tries
    '''

    if verb_to_third_person.endswith('y'):
        third_person_form = verb_to_third_person[:-1] + 'ies'
    elif verb_to_third_person.endswith(('o', 'ch', 'sh', 'x', 'z')):
        third_person_form = verb_to_third_person + 'es'
    else:
        third_person_form = verb_to_third_person + 's'

    return(third_person_form)
