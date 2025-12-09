# Jayden Murillo
# Made: 12.9.25
# Last Edit: 12.9.25

import os
import inquirer3

UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



def vigenere_cipher(phrase, key):
    encoded_phrase = ''
    for letter in phrase:
        if letter.isalpha():
            if letter.isupper():
                original_index = UPPER_ALPHABET.index(letter)
                key_index = phrase.index(letter)
                print(key_index)
                key_letter = key[key_index]
                print(key_letter)
                # index_key = UPPER_ALPHABET.index(key_letter)

            if letter.islower():
                letter.upper()
        else:
            encoded_phrase += letter



def main():
    phrase = str(input("[-] Please Input A Phrase: "))
    key = str("banana")
    vigenere_cipher(phrase,key)



if __name__ == "__main__":
    main()