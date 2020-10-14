""" Caesar Cipher
    A Caesar cipher is a simple substitution cipher in which each letter of the
    plain text is substituted with a letter found by moving n places down the
    alphabet. For example, assume the input plain text is the following:

        abcd xyz

    If the shift value, n, is 4, then the encrypted text would be the following:

        efgh bcd

    You are to write a function that accepts two arguments, a plain-text
    message and a number of letters to shift in the cipher. The function will
    return an encrypted string with all letters transformed and all
    punctuation and whitespace remaining unchanged.

    Note: You can assume the plain text is all lowercase ASCII except for
    whitespace and punctuation.
"""

import string

def the_best_caesar(plain_text, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = str.maketrans(letters, mask)
    return plain_text.translate(trantab)

def shift2_n(letter, amount):
    if letter not in string.ascii_lowercase:
        return letter
    new_letter = ord(letter) + amount
    while new_letter > ord("z"):
        new_letter -= 26
    while new_letter < ord("a"):
        new_letter += 26
    return chr(new_letter)

def caesar2(message, amount):
    enc_list = [shift2_n(letter, amount) for letter in message]
    return "".join(enc_list)

def shift3_n(letter, table):
    try:
        index = string.ascii_lowercase.index(letter)
        return table[index]
    except ValueError:
        return letter

def caesar3(message, amount):
    amount = amount % 26
    table = string.ascii_lowercase[amount:] + string.ascii_lowercase[:amount]
    enc_list = [shift3_n(letter, table) for letter in message]
    return "".join(enc_list)

print(the_best_caesar("Alicja", 3))
print(caesar2("Alicja", 3))
print(caesar3("Alicja", 3))