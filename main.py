# Jayden Murillo
# Made: 12.9.25
# Last Edit: 12.9.25

import os
# import inquirer3

UPPER_CASE = 65
LOWER_CASE = 97
ALPHABET_SIZE = 26
phrase = str(input("[-] Please Input A Phrase: "))
key = "banana"

def get_key_index(key,phrase):
    if range(len(key)) == range(len(phrase)):
        list_indexes = []
        for i in key:
            if i.isalpha():
                # charset = (UPPER_CASE if i.isupper() else LOWER_CASE)
                # indexes = (ord(i) - charset)
                list_indexes.append(i)
        return list_indexes

    else:
        for i in range(len(phrase) - len(key)):
            key_add = (key[i % len(key)])
            key += key_add
        return "".join(key)

key_index = get_key_index(key,phrase)
# print(key_index)

def vigenere_cipher(phrase, key_index):
    encoded_phrase = ''
    for letter in range(len(phrase)):
        if phrase[letter].isalpha():
            print(phrase[letter].lower())
            phrase_lower = phrase[letter].lower()
            charset = (UPPER_CASE if phrase[letter].isupper() else LOWER_CASE)
            
            # print((ord(phrase[letter]) - charset + (ord(key_index[letter])) - charset) % ALPHABET_SIZE + charset)
            print(f"Ordinal of phrase letter: {ord(phrase_lower)}\n"
                  f"Ordinal value of key letter: {ord(key_index[letter])}\n"
                  f"Shift value: {ord(key_index[letter]) - charset}\n"
                  f"Result value: {(ord(phrase[letter]) - charset + (ord(key_index[letter])) - charset) % (ALPHABET_SIZE + charset)}")
            encoded_phrase += chr((ord(phrase_lower) - charset + (ord(key_index[letter])) - charset) % (ALPHABET_SIZE + charset))
            
        else:
            encoded_phrase += letter

    return encoded_phrase



def main():
    encoded_phrase = vigenere_cipher(phrase,key_index)
    print(encoded_phrase)


if __name__ == "__main__":
    main()