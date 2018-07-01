#Caesar cipher
def caesar_cipher(string, shift):
    english_alphabet = "abcdefghijklmnopqrstuvwxyz"
    russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    converted_string = ""
    for symbol in string:
        pointer = english_alphabet.find( symbol.lower() )
        if pointer != -1:
            if symbol.isupper():
                converted_string += english_alphabet[ (pointer + shift) % 26 ].upper()
            else:
                converted_string += english_alphabet[ (pointer + shift) % 26 ]
            continue

        pointer = russian_alphabet.find( symbol.lower() )
        if pointer != -1:
            if symbol.isupper():
                converted_string += russian_alphabet[ (pointer + shift) % 33 ].upper()

            else:
                converted_string += russian_alphabet[ (pointer + shift) % 33 ]

            continue

        converted_string += symbol

    return converted_string
