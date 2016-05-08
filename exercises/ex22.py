#!/usr/bin/python


caesar_key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t',
              'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a',
              'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h',
              'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O',
              'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V',
              'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C',
              'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J',
              'X':'K', 'Y':'L', 'Z':'M'}


def caesar_cipher_decoder(string_to_decode):
    '''
    Decodes caesar ciphers
    '''

    decoded_string = ''

    for char in string_to_decode:
        if char in caesar_key:
            decoded_string += caesar_key[char]
        else:
            decoded_string += char

    return(decoded_string)


def caesar_cipher_encoder(string_to_encode):
    '''
    Encode caesar ciphers
    '''

    encoded_string = ''

    for char in string_to_encode:
        if char in '!?. ':
            encoded_string += char
        for key, value in caesar_key.items():
            if char == value:
                encoded_string += key

    return(encoded_string)

