# Jayden Murillo
# Made: 12.9.25
# Last Edit: 12.9.25

import os
import inquirer3

UPPER_CASE = 65
LOWER_CASE = 97
ALPHABET_SIZE = 26

# def get_key_index(key):
#     for i in key:
#         if i.isalpha():
#             charset = (UPPER_CASE if i.isupper() else LOWER_CASE)
#             key_index = ord(i) - charset
#     return key_index


def vigenere_cipher(phrase, key):
    encoded_phrase = ''
    for letter in phrase:
        if letter.isalpha():
            charset = (UPPER_CASE if letter.isupper() else LOWER_CASE)
            for i in key:
                key_index = (ord(i) - charset)
                print(key_index)

            
            encoded_phrase += chr((ord(letter) - charset + key_index) % ALPHABET_SIZE + charset)
            print(encoded_phrase)
            
        else:
            encoded_phrase += letter



def main():
    phrase = str(input("[-] Please Input A Phrase: "))
    key = str("banana")
    vigenere_cipher(phrase,key)



if __name__ == "__main__":
    main()