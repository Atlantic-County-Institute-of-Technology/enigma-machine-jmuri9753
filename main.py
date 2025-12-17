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
                list_indexes.append(i)
        return list_indexes

    # elif len(phrase) > len(key):
    #     print(key)
    #     i = 0
    #     while i < len(phrase) - len(key):  
    #         i += 1

    else:
        print(key)
        for j in range(len(key)):
            for i in range(len(phrase)):
                print(key[j % len(key)])
            

        return "".join(key)

key_index = get_key_index(key,phrase)

def vigenere_cipher_encode(phrase, key_index):
    encoded_phrase = ''
    for letter in range(len(phrase)):
        print(f"{phrase[letter], key_index[letter]} \n")
        if phrase[letter].isalpha():
            phrase_lower = phrase[letter].lower()
            charset = (UPPER_CASE if phrase_lower.isupper() else LOWER_CASE)

            if phrase[letter] == phrase_lower:
                encoded_phrase += chr((ord(phrase_lower) - charset + (ord(key_index[letter]) - charset)) % ALPHABET_SIZE + charset)
            else:
                encoded_phrase += chr((ord(phrase_lower) - charset + (ord(key_index[letter]) - charset)) % ALPHABET_SIZE + charset).upper()
        else:
            encoded_phrase += phrase[letter]

    return encoded_phrase


def vigenere_cipher_decode(encoded_phrase, key_index):
    decoded_phrase = ''
    for letter in range(len(encoded_phrase)):
        if phrase[letter].isalpha():
            phrase_lower = encoded_phrase[letter].lower()
            charset = (UPPER_CASE if phrase_lower.isupper() else LOWER_CASE)

            if encoded_phrase[letter] == phrase_lower:
                decoded_phrase += chr((ord(phrase_lower) - charset - (ord(key_index[letter]) - charset)) % ALPHABET_SIZE + charset)
            else:
                decoded_phrase += chr((ord(phrase_lower) - charset - (ord(key_index[letter]) - charset)) % ALPHABET_SIZE + charset).upper()
        else:
            decoded_phrase += encoded_phrase[letter]

    return decoded_phrase

def main():
    get_key_index(phrase, key)
    # encoded_phrase = vigenere_cipher_encode(phrase,key_index)
    # decoded_phrase = vigenere_cipher_decode(encoded_phrase, key_index)
    # print(encoded_phrase)
    # print(decoded_phrase)


if __name__ == "__main__":
    main()