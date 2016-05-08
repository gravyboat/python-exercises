from nose.tools import *
from exercises import ex22


def test_caesar_cipher_decoder():
    '''
    Make sure our caesar cipher decodes the right string
    '''

    decoded_cipher_output = ex22.caesar_cipher_decoder('Pnrfne pvcure?')
    assert_equal(decoded_cipher_output, 'Caesar cipher?')


def test_caesar_cipher_encoder():
    '''
    Make sure our caesar cipher encodes the right string
    '''

    encoded_cipher_output = ex22.caesar_cipher_encoder('Caesar cipher?')
    assert_equal(encoded_cipher_output, 'Pnrfne pvcure?')
