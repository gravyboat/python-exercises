#!/usr/bin/python


def max_in_list(list_of_numbers):
    '''
    Finds the largest number in a list
    '''

    biggest_num = 0

    for i in list_of_numbers:
        if i > biggest_num:
            biggest_num = i
    return(biggest_num)

