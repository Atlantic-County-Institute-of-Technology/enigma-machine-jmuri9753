# Jayden Murillo
# Made: 12.9.25
# Last Edit: 12.9.25

import os
# import inquirer3

UPPER_CASE = 65
LOWER_CASE = 97
ALPHABET_SIZE = 26
phrase = str(input("[-] Please Input A Phrase: "))
key = str("Banana")

def get_key_index(key,phrase):
    if range(len(key)) == range(len(phrase)):
        list_indexes = []
        for i in key:
            if i.isalpha():
                charset = (UPPER_CASE if i.isupper() else LOWER_CASE)
                indexes = (ord(i) - charset)
                list_indexes.append(indexes)
        return list_indexes

    else:
        pass

key_index = get_key_index(key,phrase)


def vigenere_cipher(phrase, key_index):
    encoded_phrase = ''
    for letter in range(len(phrase)):
        if phrase[letter].isalpha():
            charset = (UPPER_CASE if phrase[letter].isupper() else LOWER_CASE)

            
            encoded_phrase += chr((ord(phrase[letter]) - charset + key_index[letter]) % ALPHABET_SIZE + charset)
            
        else:
            encoded_phrase += letter

    return encoded_phrase



def main():
    encoded_phrase = vigenere_cipher(phrase,key_index)
    print(encoded_phrase)


if __name__ == "__main__":
    main()