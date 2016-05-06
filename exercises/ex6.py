#!/usr/bin/python

def sum(*args):
    '''
    Adds all arguments together
    '''

    final_sum = 0
    for number in args:
        final_sum += number
    return(final_sum)

def multiply(*args):
    '''
    Multiplies all arguments together
    '''

    final_sum = 1

    for number in args:
        final_sum = final_sum * number
    return(final_sum)
