from nose.tools import *
from exercises import ex22


def test_caesar_cipher_decoder():
    '''
    Make sure our caesar cipher equals the correct string
    '''

    decoded_cipher_output = ex22.caesar_cipher_decoder('Pnrfne pvcure?')
    assert_equal(decoded_cipher_output, 'Caesar cipher?')

