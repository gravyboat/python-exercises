#!/usr/bin/python


def max_of_three(val_one, val_two, val_three):
    '''
    Return the max of three values
    '''

    if val_one > val_two and val_one > val_three:
        return(val_one)
    elif val_two > val_one and val_two > val_three:
        return(val_two)
    elif val_three > val_one and val_three > val_two:
        return(val_three)

