#!/usr/bin/python


def bottles_of_beer(bottle_count):
    '''
    Sings the traditional 99 bottles of beer song
    '''

    for i in range(bottle_count, 0, -1):
        print('{0} bottles of beer on the wall, {0} bottles of beer.'.format(i))
        print('Take one down, pass it around, {0} bottles of beer on the wall.'.format(i - 1))

